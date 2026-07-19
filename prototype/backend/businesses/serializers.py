from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone

from .models import (
    Account,
    AccountUser,
    Business,
    Catalogue,
    CatalogueItem,
    CaseStudy,
    FAQ,
    FollowUpTask,
    Inquiry,
    Lead,
    MediaAsset,
    MessageTemplate,
    OperatorNote,
    PageEvent,
    Payment,
    ScoreReason,
    SetupProject,
    Testimonial,
    TrustProof,
)

User = get_user_model()


class CatalogueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogueItem
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class TrustProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustProof
        fields = "__all__"


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = "__all__"


class CatalogueSerializer(serializers.ModelSerializer):
    items = CatalogueItemSerializer(many=True, read_only=True)
    faqs = FAQSerializer(many=True, read_only=True)

    class Meta:
        model = Catalogue
        fields = "__all__"


class SetupProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetupProject
        fields = "__all__"


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class FollowUpTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpTask
        fields = "__all__"


class MessageTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTemplate
        fields = "__all__"


class ScoreReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreReason
        fields = "__all__"


class OperatorNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatorNote
        fields = "__all__"


class BusinessSerializer(serializers.ModelSerializer):
    catalogue = CatalogueSerializer(read_only=True)
    trust_proof = TrustProofSerializer(many=True, read_only=True)
    media_assets = MediaAssetSerializer(many=True, read_only=True)
    testimonials = TestimonialSerializer(many=True, read_only=True)
    case_studies = CaseStudySerializer(many=True, read_only=True)
    setup_project = SetupProjectSerializer(read_only=True)
    leads = LeadSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    tasks = FollowUpTaskSerializer(many=True, read_only=True)
    message_templates = MessageTemplateSerializer(many=True, read_only=True)
    score_reasons = ScoreReasonSerializer(many=True, read_only=True)
    operator_notes = OperatorNoteSerializer(many=True, read_only=True)
    page_views = serializers.SerializerMethodField()
    whatsapp_clicks = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = "__all__"

    def get_page_views(self, obj):
        return obj.page_events.filter(event_type="view").count()

    def get_whatsapp_clicks(self, obj):
        return obj.page_events.filter(event_type="whatsapp_click").count()


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"


class PublicInquirySerializer(serializers.Serializer):
    business = serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())
    catalogue_item = serializers.PrimaryKeyRelatedField(
        queryset=CatalogueItem.objects.all(), required=False, allow_null=True
    )
    name = serializers.CharField(max_length=120)
    phone_number = serializers.CharField(max_length=32)
    message = serializers.CharField(required=False, allow_blank=True)
    source = serializers.CharField(required=False, default="public_page")
    expected_value = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, default=0)
    extra_context = serializers.JSONField(required=False, default=dict)


class PageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageEvent
        fields = "__all__"


# User Serializers
class UserSerializer(serializers.ModelSerializer):
    """
    User profile serializer.
    """
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone_number',
            'whatsapp_number', 'preferred_language', 'avatar',
            'is_verified', 'last_active_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'is_verified', 'last_active_at', 'created_at', 'updated_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    User registration serializer with password validation.
    """
    
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'phone_number',
            'password', 'password_confirm', 'preferred_language'
        ]
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        
        try:
            validate_password(attrs['password'])
        except Exception as e:
            raise serializers.ValidationError({"password": str(e)})
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            preferred_language=validated_data.get('preferred_language', 'en'),
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    User login serializer.
    """
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        from django.contrib.auth import authenticate
        
        user = authenticate(
            username=attrs['email'],
            password=attrs['password']
        )
        
        if not user:
            raise serializers.ValidationError(
                {"email": "Invalid email or password."}
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                {"email": "Account is disabled."}
            )
        
        attrs['user'] = user
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    """
    Password reset serializer.
    """
    
    email = serializers.EmailField()
    
    def validate_email(self, value):
        User = get_user_model()
        
        if not User.objects.filter(email=value).exists():
            return value
        
        return value


# Account Serializers
class AccountSerializer(serializers.ModelSerializer):
    """
    Account serializer.
    """
    
    class Meta:
        model = Account
        fields = [
            'id', 'name', 'slug', 'plan', 'status',
            'max_businesses', 'max_users',
            'subscription_start', 'subscription_end',
            'billing_email', 'billing_phone',
            'address', 'city', 'state', 'pincode', 'country',
            'gst_number', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'slug', 'created_at', 'updated_at',
            'max_businesses', 'max_users'
        ]


class AccountCreateSerializer(serializers.ModelSerializer):
    """
    Account creation serializer.
    """
    
    class Meta:
        model = Account
        fields = [
            'name', 'plan', 'billing_email', 'billing_phone',
            'address', 'city', 'state', 'pincode', 'country', 'gst_number'
        ]
    
    def create(self, validated_data):
        user = self.context['user']
        
        account = Account.objects.create(
            **validated_data,
            created_by=user
        )
        
        AccountUser.objects.create(
            user=user,
            account=account,
            role=AccountUser.Role.OWNER,
            invited_by=user
        )
        
        return account


class AccountUserSerializer(serializers.ModelSerializer):
    """
    Account user serializer.
    """
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = AccountUser
        fields = [
            'id', 'user', 'account', 'role',
            'is_active', 'invited_by', 'invited_at',
            'joined_at', 'last_active_at', 'created_at'
        ]
        read_only_fields = [
            'id', 'user', 'account', 'invited_at',
            'joined_at', 'last_active_at', 'created_at'
        ]


class InvitationSerializer(serializers.Serializer):
    """
    User invitation serializer.
    """
    
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=AccountUser.Role.choices)
    
    def validate_email(self, value):
        User = get_user_model()
        
        user = User.objects.filter(email=value).first()
        if user:
            account = self.context['account']
            if AccountUser.objects.filter(user=user, account=account).exists():
                raise serializers.ValidationError(
                    "User already has access to this account."
                )
        
        return value
    
    def create(self, validated_data):
        User = get_user_model()
        
        account = self.context['account']
        request = self.context['request']
        
        email = validated_data['email']
        role = validated_data['role']
        
        user = User.objects.filter(email=email).first()
        
        if user:
            account_user = AccountUser.objects.create(
                user=user,
                account=account,
                role=role,
                invited_by=request.user,
                joined_at=timezone.now()
            )
            return account_user
        else:
            account_user = AccountUser.objects.create(
                user=None,
                account=account,
                role=role,
                invited_by=request.user,
                is_active=False
            )
            return account_user
