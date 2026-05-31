from django.db.models import Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
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
    BusinessSerializer,
    FollowUpTaskSerializer,
    InquirySerializer,
    LeadSerializer,
    MessageTemplateSerializer,
    PageEventSerializer,
    PaymentSerializer,
    PublicInquirySerializer,
    SetupProjectSerializer,
)


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
