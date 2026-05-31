from django.db import models


class Business(models.Model):
    class PersonaPack(models.TextChoices):
        TUTOR = "tutor", "Tutor / Coach"
        EVENT = "event", "Event Service"
        AGENCY = "agency", "Freelancer / Agency"
        CONSULTANT = "consultant", "Consultant"
        CREATOR = "creator", "Creator"
        HOME_SERVICE = "home_service", "Home Service"

    name = models.CharField(max_length=160)
    owner_name = models.CharField(max_length=120)
    persona_pack = models.CharField(max_length=40, choices=PersonaPack.choices)
    city = models.CharField(max_length=80)
    whatsapp_number = models.CharField(max_length=32)
    public_slug = models.SlugField(unique=True)
    preferred_language = models.CharField(max_length=40, default="Hinglish")
    brand_tone = models.CharField(max_length=80, default="Friendly professional")
    payment_terms = models.TextField(blank=True)
    growth_score = models.PositiveSmallIntegerField(default=0)
    health_score = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SetupProject(models.Model):
    class Stage(models.TextChoices):
        INTAKE = "intake", "Intake"
        CATALOGUE_DRAFT = "catalogue_draft", "Catalogue Draft"
        PAGE_REVIEW = "page_review", "Page Review"
        PUBLISHED = "published", "Published"
        WEEKLY_REVIEW = "weekly_review", "Weekly Review"

    business = models.OneToOneField(Business, on_delete=models.CASCADE, related_name="setup_project")
    stage = models.CharField(max_length=40, choices=Stage.choices, default=Stage.INTAKE)
    package_name = models.CharField(max_length=80, default="Starter Pilot")
    owner_inputs_complete = models.BooleanField(default=False)
    blockers = models.TextField(blank=True)
    target_publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.business.name} - {self.get_stage_display()}"


class Catalogue(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, related_name="catalogue")
    audience = models.CharField(max_length=180)
    headline = models.CharField(max_length=240)
    subtext = models.TextField()
    primary_cta = models.CharField(max_length=80)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.business.name} catalogue"


class CatalogueItem(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=140)
    format = models.CharField(max_length=80)
    description = models.TextField()
    price_label = models.CharField(max_length=80)
    details = models.TextField(blank=True)
    timing_or_timeline = models.CharField(max_length=140, blank=True)
    terms = models.CharField(max_length=180, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class TrustProof(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="trust_proof")
    title = models.CharField(max_length=140)
    detail = models.TextField(blank=True)
    proof_type = models.CharField(max_length=60, default="testimonial")
    approved_for_public_use = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=180)
    answer = models.TextField()
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "question"]

    def __str__(self):
        return self.question


class MediaAsset(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="media_assets")
    title = models.CharField(max_length=140)
    asset_type = models.CharField(max_length=60, default="image")
    category = models.CharField(max_length=80, blank=True)
    url = models.URLField(blank=True)
    placeholder_color = models.CharField(max_length=20, default="#d9cab3")
    caption = models.CharField(max_length=220, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="testimonials")
    customer_name = models.CharField(max_length=120)
    customer_context = models.CharField(max_length=120, blank=True)
    quote = models.TextField()
    approved_for_public_use = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "customer_name"]

    def __str__(self):
        return self.customer_name


class CaseStudy(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="case_studies")
    title = models.CharField(max_length=160)
    client_context = models.CharField(max_length=140)
    problem = models.TextField()
    work_done = models.TextField()
    outcome = models.TextField()
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class PageEvent(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="page_events")
    event_type = models.CharField(max_length=40)
    source = models.CharField(max_length=80, blank=True)
    catalogue_item = models.ForeignKey(CatalogueItem, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Inquiry(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="inquiries")
    catalogue_item = models.ForeignKey(
        CatalogueItem, on_delete=models.SET_NULL, null=True, blank=True, related_name="inquiries"
    )
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=32)
    message = models.TextField(blank=True)
    source = models.CharField(max_length=80, default="public_page")
    extra_context = models.JSONField(default=dict, blank=True)
    is_qualified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.business.name}"


class Lead(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="leads")
    inquiry = models.OneToOneField(Inquiry, on_delete=models.SET_NULL, null=True, blank=True, related_name="lead")
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=32)
    interested_service = models.CharField(max_length=140)
    source = models.CharField(max_length=80)
    status = models.CharField(max_length=80)
    expected_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    next_action = models.CharField(max_length=220, blank=True)
    follow_up_age_days = models.PositiveSmallIntegerField(default=0)
    urgency_reason = models.CharField(max_length=220, blank=True)
    next_follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FollowUpTask(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="tasks")
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    title = models.CharField(max_length=160)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, default="medium")
    status = models.CharField(max_length=40, default="pending")
    suggested_message = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="customers")
    lead = models.OneToOneField(Lead, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=32, blank=True)
    active_status = models.CharField(max_length=40, default="active")
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    class Status(models.TextChoices):
        UNPAID = "unpaid", "Unpaid"
        PART_PAID = "part_paid", "Part Paid"
        PAID = "paid", "Paid"
        OVERDUE = "overdue", "Overdue"

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="payments")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")
    lead = models.ForeignKey(Lead, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")
    payer_name = models.CharField(max_length=120)
    service_name = models.CharField(max_length=140)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.UNPAID)
    age_days = models.PositiveSmallIntegerField(default=0)
    urgency_reason = models.CharField(max_length=220, blank=True)
    payment_mode = models.CharField(max_length=60, blank=True)
    reference_note = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return f"{self.payer_name} - {self.amount_due}"


class MessageTemplate(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="message_templates")
    message_type = models.CharField(max_length=80)
    tone = models.CharField(max_length=40, default="friendly")
    language = models.CharField(max_length=40, default="Hinglish")
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.message_type


class ScoreSnapshot(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="score_snapshots")
    growth_score = models.PositiveSmallIntegerField(default=0)
    health_score = models.PositiveSmallIntegerField(default=0)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ScoreReason(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="score_reasons")
    score_type = models.CharField(max_length=40)
    label = models.CharField(max_length=120)
    detail = models.CharField(max_length=240)
    severity = models.CharField(max_length=20, default="info")

    def __str__(self):
        return f"{self.business.name} - {self.label}"


class OperatorNote(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="operator_notes")
    note_type = models.CharField(max_length=60, default="setup")
    body = models.TextField()
    is_blocker = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - {self.note_type}"
