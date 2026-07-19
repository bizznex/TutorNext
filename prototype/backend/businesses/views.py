from django.db.models import Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import (
    Account,
    AccountUser,
    Business,
    FollowUpTask,
    Inquiry,
    Lead,
    MessageTemplate,
    PageEvent,
    Payment,
    SetupProject,
)
from .personas import PERSONA_PACKS, fill_template
from .serializers import (
    AccountSerializer,
    AccountUserSerializer,
    AccountCreateSerializer,
    BusinessSerializer,
    FollowUpTaskSerializer,
    InquirySerializer,
    InvitationSerializer,
    LeadSerializer,
    MessageTemplateSerializer,
    PageEventSerializer,
    PasswordResetSerializer,
    PaymentSerializer,
    PublicInquirySerializer,
    SetupProjectSerializer,
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserSerializer,
)

User = get_user_model()


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().prefetch_related(
        "catalogue__items",
        "trust_proof",
        "leads",
        "payments",
        "tasks",
        "message_templates",
        "page_events",
    )
    serializer_class = BusinessSerializer

    @action(detail=True, methods=["post"])
    def page_event(self, request, pk=None):
        business = self.get_object()
        serializer = PageEventSerializer(data={**request.data, "business": business.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        business = self.get_object()
        pending = business.payments.exclude(status=Payment.Status.PAID)
        data = {
            "open_leads": business.leads.exclude(status__in=["Enrolled", "Booked", "Won", "Lost"]).count(),
            "follow_ups": business.tasks.filter(status="pending").count(),
            "pending_amount": pending.aggregate(total=Sum("amount_due"))["total"] or 0,
            "page_views": business.page_events.filter(event_type="view").count(),
            "whatsapp_clicks": business.page_events.filter(event_type="whatsapp_click").count(),
            "growth_score": business.growth_score,
            "health_score": business.health_score,
        }
        return Response(data)


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().select_related("business", "catalogue_item")
    serializer_class = InquirySerializer

    @action(detail=False, methods=["post"])
    def capture(self, request):
        serializer = PublicInquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        business = data["business"]
        item = data.get("catalogue_item")
        pack = PERSONA_PACKS.get(business.persona_pack, PERSONA_PACKS["tutor"])

        inquiry = Inquiry.objects.create(
            business=business,
            catalogue_item=item,
            name=data["name"],
            phone_number=data["phone_number"],
            message=data.get("message", ""),
            source=data.get("source", "public_page"),
            extra_context=data.get("extra_context", {}),
            is_qualified=True,
        )
        service_name = item.name if item else "selected service"
        lead = Lead.objects.create(
            business=business,
            inquiry=inquiry,
            name=inquiry.name,
            phone_number=inquiry.phone_number,
            interested_service=service_name,
            source=inquiry.source,
            status=pack["first_status"],
            expected_value=data.get("expected_value", 0),
            next_action=pack["first_action"],
        )
        FollowUpTask.objects.create(
            business=business,
            lead=lead,
            title=f"Reply to {lead.name}",
            priority="high",
            suggested_message=fill_template(pack["messages"]["first_reply"], name=lead.name, service=service_name),
        )
        PageEvent.objects.create(business=business, catalogue_item=item, event_type="inquiry_submit", source=inquiry.source)

        return Response(
            {
                "inquiry": InquirySerializer(inquiry).data,
                "lead": LeadSerializer(lead).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().select_related("business", "inquiry")
    serializer_class = LeadSerializer

    @action(detail=True, methods=["post"])
    def set_status(self, request, pk=None):
        lead = self.get_object()
        lead.status = request.data.get("status", lead.status)
        lead.next_action = request.data.get("next_action", lead.next_action)
        lead.save(update_fields=["status", "next_action", "updated_at"])
        return Response(LeadSerializer(lead).data)

    @action(detail=True, methods=["get"])
    def suggested_message(self, request, pk=None):
        lead = self.get_object()
        pack = PERSONA_PACKS.get(lead.business.persona_pack, PERSONA_PACKS["tutor"])
        message = fill_template(pack["messages"]["follow_up"], name=lead.name, service=lead.interested_service)
        return Response({"message": message})


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().select_related("business", "lead", "customer")
    serializer_class = PaymentSerializer

    @action(detail=True, methods=["post"])
    def mark_paid(self, request, pk=None):
        payment = self.get_object()
        amount_paid = request.data.get("amount_paid")
        payment.status = Payment.Status.PAID
        payment.amount_paid = amount_paid if amount_paid is not None else payment.amount_due
        payment.save(update_fields=["status", "amount_paid"])
        return Response(PaymentSerializer(payment).data)

    @action(detail=True, methods=["get"])
    def reminder(self, request, pk=None):
        payment = self.get_object()
        pack = PERSONA_PACKS.get(payment.business.persona_pack, PERSONA_PACKS["tutor"])
        message = fill_template(
            pack["messages"]["payment"],
            name=payment.payer_name,
            service=payment.service_name,
            amount=int(payment.amount_due),
        )
        return Response({"message": message})


class MessageTemplateViewSet(viewsets.ModelViewSet):
    queryset = MessageTemplate.objects.all().select_related("business")
    serializer_class = MessageTemplateSerializer


class SetupProjectViewSet(viewsets.ModelViewSet):
    queryset = SetupProject.objects.all().select_related("business")
    serializer_class = SetupProjectSerializer


class PageEventViewSet(viewsets.ModelViewSet):
    queryset = PageEvent.objects.all().select_related("business", "catalogue_item")
    serializer_class = PageEventSerializer


# ============================================================================
# Auth Views - ContexureEarth Tutor
# ============================================================================

class UserRegistrationView(viewsets.GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        account = Account.objects.create(
            name=f"{user.get_full_name()}'s Tutor Studio",
            slug=user.email.split('@')[0],
            billing_email=user.email,
            created_by=user
        )
        
        AccountUser.objects.create(
            user=user,
            account=account,
            role=AccountUser.Role.OWNER,
            invited_by=user
        )
        
        return Response({
            'user': UserSerializer(user).data,
            'account': account.slug,
            'message': 'Registration successful. Please login to ContexureEarth Tutor.'
        }, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]


class UserLogoutView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        from rest_framework_simplejwt.tokens import RefreshToken
        
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out.'})
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileView(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PasswordResetView(viewsets.GenericViewSet):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def request_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'message': 'Password reset link sent to your email.'
        })


# ============================================================================
# Account Views - ContexureEarth Tutor
# ============================================================================

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Account.objects.filter(
            users__user=self.request.user,
            users__is_active=True
        ).distinct()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = AccountCreateSerializer(
            data=request.data,
            context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        
        return Response(
            self.get_serializer(account).data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=True, methods=['post'])
    def invite_user(self, request, pk=None):
        account = self.get_object()
        serializer = InvitationSerializer(
            data=request.data,
            context={'account': account, 'request': request}
        )
        serializer.is_valid(raise_exception=True)
        account_user = serializer.save()
        
        return Response(
            AccountUserSerializer(account_user).data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        account = self.get_object()
        users = AccountUser.objects.filter(
            account=account,
            is_active=True
        )
        serializer = AccountUserSerializer(users, many=True)
        return Response(serializer.data)


class AccountUserViewSet(viewsets.ModelViewSet):
    serializer_class = AccountUserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        business_id = self.kwargs.get('business_pk')
        if business_id:
            business = Business.objects.get(pk=business_id)
            return AccountUser.objects.filter(
                account=business.account
            )
        return AccountUser.objects.none()
