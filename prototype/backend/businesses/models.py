from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    This replaces the default User model and adds tutor-specific fields.
    """
    
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Optional username"
    )
    
    email = models.EmailField(
        unique=True,
        help_text="Primary identifier for login"
    )
    
    phone_number = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text="User's phone number for notifications"
    )
    
    preferred_language = models.CharField(
        max_length=40,
        default="en",
        choices=[
            ("en", "English"),
            ("hi", "Hindi"),
            ("hinglish", "Hinglish"),
            ("bn", "Bengali"),
        ],
        help_text="Preferred language for UI and messages"
    )
    
    whatsapp_number = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text="WhatsApp number for business notifications"
    )
    
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        help_text="User profile picture"
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text="Email/phone verified"
    )
    
    last_active_at = models.DateTimeField(
        auto_now=True,
        help_text="Last activity timestamp"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="User creation timestamp"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update timestamp"
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]


class Account(models.Model):
    """
    Represents a billing/subscription unit.
    
    An account can have multiple businesses and multiple users.
    """
    
    class PlanType(models.TextChoices):
        FREE = "free", "Free"
        STARTER = "starter", "Starter"
        PRO = "pro", "Pro"
        ENTERPRISE = "enterprise", "Enterprise"
    
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        SUSPENDED = "suspended", "Suspended"
        CANCELLED = "cancelled", "Cancelled"
    
    name = models.CharField(
        max_length=120,
        help_text="Account name (e.g., 'Ananya's Tutoring Business')"
    )
    
    slug = models.SlugField(
        unique=True,
        help_text="URL-friendly account identifier"
    )
    
    plan = models.CharField(
        max_length=20,
        choices=PlanType.choices,
        default=PlanType.FREE,
        help_text="Subscription plan"
    )
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text="Account status"
    )
    
    max_businesses = models.PositiveSmallIntegerField(
        default=1,
        help_text="Maximum number of businesses allowed"
    )
    
    max_users = models.PositiveSmallIntegerField(
        default=1,
        help_text="Maximum number of users allowed"
    )
    
    subscription_start = models.DateField(
        null=True,
        blank=True,
        help_text="Subscription start date"
    )
    
    subscription_end = models.DateField(
        null=True,
        blank=True,
        help_text="Subscription end date"
    )
    
    billing_email = models.EmailField(
        help_text="Email for billing communications"
    )
    
    billing_phone = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text="Phone for billing communications"
    )
    
    address = models.TextField(
        blank=True,
        null=True,
        help_text="Billing address"
    )
    
    city = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="City for billing"
    )
    
    state = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="State for billing"
    )
    
    pincode = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Pincode for billing"
    )
    
    country = models.CharField(
        max_length=80,
        default="India",
        help_text="Country for billing"
    )
    
    gst_number = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        help_text="GST registration number"
    )
    
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_accounts",
        help_text="User who created this account"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Account creation timestamp"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update timestamp"
    )
    
    def __str__(self):
        return f"{self.name} ({self.slug})"
    
    def is_active(self):
        return self.status == self.Status.ACTIVE
    
    def can_add_business(self):
        return self.businesses.count() < self.max_businesses
    
    def can_add_user(self):
        return self.users.count() < self.max_users


class AccountUser(models.Model):
    """
    Maps users to accounts with role-based permissions.
    
    This is a through model for the User-Account many-to-many relationship.
    """
    
    class Role(models.TextChoices):
        OWNER = "owner", "Owner"
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        OPERATOR = "operator", "Operator"
        VIEWER = "viewer", "Viewer"
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="account_memberships",
        help_text="The user"
    )
    
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="users",
        help_text="The account"
    )
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER,
        help_text="User's role in this account"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this membership is active"
    )
    
    invited_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="invited_users",
        help_text="User who invited this user"
    )
    
    invited_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Invitation timestamp"
    )
    
    joined_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When user accepted invitation"
    )
    
    last_active_at = models.DateTimeField(
        auto_now=True,
        help_text="Last activity in this account"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Membership creation timestamp"
    )
    
    class Meta:
        unique_together = [['user', 'account']]
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} ({self.get_role_display()}) @ {self.account.name}"
    
    def is_owner(self):
        return self.role == self.Role.OWNER
    
    def is_admin(self):
        return self.role in [self.Role.OWNER, self.Role.ADMIN]
    
    def can_manage_users(self):
        return self.is_admin()
    
    def can_manage_businesses(self):
        return self.role in [self.Role.OWNER, self.Role.ADMIN, self.Role.MANAGER]
    
    def can_view_data(self):
        return self.is_active
    
    def can_edit_data(self):
        return self.is_active and self.role in [self.Role.OWNER, self.Role.ADMIN, self.Role.MANAGER]


class Business(models.Model):
    class PersonaPack(models.TextChoices):
        TUTOR = "tutor", "Tutor / Coach"
        EVENT = "event", "Event Service"
        AGENCY = "agency", "Freelancer / Agency"
        CONSULTANT = "consultant", "Consultant"
        CREATOR = "creator", "Creator"
        HOME_SERVICE = "home_service", "Home Service"

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="businesses",
        help_text="Account this business belongs to"
    )
    
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="created_businesses",
        help_text="User who created this business"
    )
    
    assigned_users = models.ManyToManyField(
        User,
        related_name="assigned_businesses",
        blank=True,
        help_text="Users with access to this business"
    )
    
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
    
    is_public = models.BooleanField(
        default=False,
        help_text="Whether this business page is publicly accessible"
    )
    
    custom_domain = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Custom domain for this business (e.g., ananya.bizznexx.com)"
    )

    def __str__(self):
        return f"{self.name} ({self.account.slug})"
    
    def get_absolute_url(self):
        if self.custom_domain:
            return f"https://{self.custom_domain}"
        return f"https://app.bizznexx.com/b/{self.public_slug}"


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
