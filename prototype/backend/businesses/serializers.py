from rest_framework import serializers

from .models import (
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
