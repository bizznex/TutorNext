# D-002: Tenant/Account Model Definition

**Status:** Done  
**Owner:** BE/SEC  
**Priority:** P0  
**Date:** 2026-07-19

## Overview

This document defines the **tenant/account model** for ContexureEarth Tutor. This is a **critical foundation** that must be implemented before any production deployment with real user data.

**Key Principle:** Every piece of data must be **isolated by tenant** to prevent data leakage between businesses.

---

## 1. Requirements

### Functional Requirements

1. **Multi-tenancy:** Support multiple independent businesses
2. **User-Business Relationship:** A user can own/manage multiple businesses
3. **Role-Based Access:** Different permissions for owners, operators, admins
4. **Data Isolation:** Tenants cannot access each other's data
5. **Account Management:** Create, read, update, delete accounts
6. **Business Management:** Create, read, update, delete businesses within an account
7. **User Invitation:** Invite users to manage businesses
8. **Audit Trail:** Track who did what and when

### Non-Functional Requirements

1. **Performance:** Tenant filtering should not significantly impact query performance
2. **Scalability:** Support thousands of tenants
3. **Security:** No cross-tenant data access possible
4. **Maintainability:** Clear, understandable model structure

---

## 2. Design Decisions

### Decision 1: Multi-tenancy Strategy

**Chosen:** **Schema-based multi-tenancy** (recommended for PostgreSQL)

**Alternatives Considered:**
- **Shared Schema (Filter by tenant_id):** Simpler but requires discipline
- **Separate Database:** Overkill for current scale
- **Separate Schema:** Good isolation, complex to manage

**Rationale:**
- PostgreSQL supports schemas natively
- Clean data isolation at database level
- Easy to backup/restore individual tenants
- Can migrate to separate databases later if needed
- Django has good support via `django-tenants` or custom middleware

**However:** For MVP simplicity and given current Django structure, we'll use **shared schema with tenant_id filtering** initially, with a migration path to schema-based later.

### Decision 2: Account vs Business

**Chosen:** **Account contains Businesses, User belongs to Account**

```
Account (Billing/Subscription Unit)
└── Business (Individual Tutor/Coaching Center)
    └── User (Person with access)
```

**Rationale:**
- An account represents a **billing unit** (one subscription)
- An account can have **multiple businesses** (e.g., tutor with 2 coaching centers)
- A user belongs to an **account** and has access to its businesses
- Simplifies billing and subscription management

### Decision 3: User Model

**Chosen:** **Extend Django's AbstractUser**

**Rationale:**
- Full control over user fields
- Can add custom fields (phone, language preference)
- Compatible with Django admin
- Works with DRF authentication

### Decision 4: Authentication Method

**Chosen:** **JWT (JSON Web Tokens) via SimpleJWT**

**Rationale:**
- Stateless (scales well)
- Works well with SPAs (React frontend)
- Refresh token support
- Industry standard
- Good Django/DRF support

---

## 3. Data Model

### 3.1 User Model

**File:** `businesses/models.py` (new section)

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    This replaces the default User model and adds tutor-specific fields.
    """
    
    # Remove username requirement, use email as primary identifier
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
```

### 3.2 Account Model

```python
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
```

### 3.3 AccountUser Model (Many-to-Many with Roles)

```python
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
```

### 3.4 Business Model Updates

**File:** `businesses/models.py` (update existing Business model)

```python
class Business(models.Model):
    # ... existing fields ...
    
    # New fields for tenant isolation
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
    
    # ... rest of existing fields ...
    
    def __str__(self):
        return f"{self.name} ({self.account.slug})"
    
    def get_absolute_url(self):
        if self.custom_domain:
            return f"https://{self.custom_domain}"
        return f"https://app.bizznexx.com/b/{self.public_slug}"
```

### 3.5 Tenant-Aware Mixin

**File:** `businesses/models.py` (new)

```python
class TenantAwareModel(models.Model):
    """
    Abstract base class for models that need tenant isolation.
    
    Adds account and business fields to ensure data isolation.
    """
    
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="%(class)s_accounts",
        help_text="Account this record belongs to"
    )
    
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="%(class)s_businesses",
        help_text="Business this record belongs to"
    )
    
    class Meta:
        abstract = True
```

### 3.6 Updated Models with Tenant Awareness

All existing models that are business-specific should either:
1. Have a `business` ForeignKey (already present in most)
2. Or inherit from `TenantAwareModel`

**Models that need updates:**
- `SetupProject` - Already has `business` FK (good)
- `Catalogue` - Already has `business` FK (good)
- `CatalogueItem` - Already has `catalogue` FK which has business (good)
- `TrustProof` - Already has `business` FK (good)
- `FAQ` - Has `catalogue` FK which has business (good)
- `MediaAsset` - Already has `business` FK (good)
- `Testimonial` - Already has `business` FK (good)
- `CaseStudy` - Already has `business` FK (good)
- `PageEvent` - Already has `business` FK (good)
- `Inquiry` - Already has `business` FK (good)
- `Lead` - Already has `business` FK (good)
- `FollowUpTask` - Already has `business` FK (good)
- `Customer` - Already has `business` FK (good)
- `Payment` - Already has `business` FK (good)
- `MessageTemplate` - Already has `business` FK (good)
- `ScoreSnapshot` - Already has `business` FK (good)
- `ScoreReason` - Already has `business` FK (good)
- `OperatorNote` - Already has `business` FK (good)

**All models are already business-scoped!** This is excellent - we just need to add the account relationship.

---

## 4. Authentication Model

### 4.1 JWT Configuration

**File:** `bizznexx_backend/settings.py` (additions)

```python
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    ...
]

# Add JWT settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    
    'JTI_CLAIM': 'jti',
    
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Update REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

### 4.2 Custom Permission Classes

**File:** `businesses/permissions.py` (updates)

```python
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrBetaKey(BasePermission):
    """
    Allows access if:
    1. User is authenticated (JWT), OR
    2. Valid beta API key is provided (for public pages)
    """
    
    def has_permission(self, request, view):
        # Check JWT authentication first
        if request.user and request.user.is_authenticated:
            return True
        
        # Fall back to beta API key for public endpoints
        from django.conf import settings
        expected_key = getattr(settings, "BIZZNEXX_BETA_API_KEY", "")
        if not expected_key:
            return True  # Dev mode
        return request.headers.get("X-BizzNexx-Beta-Key") == expected_key


class IsBusinessOwner(BasePermission):
    """
    Check if user is owner/admin of the business.
    """
    
    def has_object_permission(self, request, view, obj):
        # obj should be a Business or have a business attribute
        from .models import Business, AccountUser
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        business = obj if isinstance(obj, Business) else getattr(obj, 'business', None)
        if not business:
            return False
        
        # Check if user has access to this business
        account_user = AccountUser.objects.filter(
            user=request.user,
            account=business.account,
            is_active=True
        ).first()
        
        if not account_user:
            return False
        
        # Owner or admin can do anything
        return account_user.is_admin()


class IsBusinessUser(BasePermission):
    """
    Check if user has any access to the business.
    """
    
    def has_object_permission(self, request, view, obj):
        from .models import Business, AccountUser
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        business = obj if isinstance(obj, Business) else getattr(obj, 'business', None)
        if not business:
            return False
        
        return AccountUser.objects.filter(
            user=request.user,
            account=business.account,
            is_active=True
        ).exists()


class TenantIsolationPermission(BasePermission):
    """
    Ensures users can only access their own tenant's data.
    
    This should be applied to all business-scoped endpoints.
    """
    
    def has_permission(self, request, view):
        # For list views, filter queryset
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
            if request.user and request.user.is_authenticated:
                # Filter to user's businesses
                from .models import AccountUser, Business
                account_ids = AccountUser.objects.filter(
                    user=request.user,
                    is_active=True
                ).values_list('account_id', flat=True)
                
                business_ids = Business.objects.filter(
                    account_id__in=account_ids
                ).values_list('id', flat=True)
                
                # Apply filter to queryset
                view.queryset = queryset.filter(business_id__in=business_ids)
        
        return True
    
    def has_object_permission(self, request, view, obj):
        from .models import Business
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        business = obj if isinstance(obj, Business) else getattr(obj, 'business', None)
        if not business:
            return False
        
        from .models import AccountUser
        return AccountUser.objects.filter(
            user=request.user,
            account=business.account,
            is_active=True
        ).exists()
```

---

## 5. API Endpoints

### 5.1 Authentication Endpoints

**File:** `businesses/views/auth.py` (new)

```python
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    PasswordResetSerializer,
)

User = get_user_model()


class UserRegistrationView(viewsets.GenericViewSet):
    """
    User registration endpoint.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        # Create account for this user
        from .models import Account, AccountUser
        account = Account.objects.create(
            name=f"{user.get_full_name()}'s Account",
            slug=user.email.split('@')[0],
            billing_email=user.email,
            created_by=user
        )
        
        # Make user owner of the account
        AccountUser.objects.create(
            user=user,
            account=account,
            role=AccountUser.Role.OWNER,
            invited_by=user
        )
        
        return Response({
            'user': UserSerializer(user).data,
            'account': account.slug,
            'message': 'Registration successful. Please login.'
        }, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    """
    User login endpoint with custom response.
    """
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]


class UserLogoutView(viewsets.GenericViewSet):
    """
    User logout endpoint (adds token to blacklist).
    """
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
    """
    Current user profile management.
    """
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
    """
    Password reset functionality.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def request_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # In production, send email with reset link
        # For now, just return success
        return Response({
            'message': 'Password reset link sent to your email.'
        })
    
    @action(detail=False, methods=['post'])
    def confirm_reset(self, request):
        # Implement password reset confirmation
        pass
```

### 5.2 Account Endpoints

**File:** `businesses/views/accounts.py` (new)

```python
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Account, AccountUser, Business
from .serializers import (
    AccountSerializer,
    AccountUserSerializer,
    AccountCreateSerializer,
    InvitationSerializer,
)
from .permissions import IsBusinessOwner, IsBusinessUser


class AccountViewSet(viewsets.ModelViewSet):
    """
    Account management endpoints.
    """
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Users can only see their own accounts
        return Account.objects.filter(
            users__user=self.request.user,
            users__is_active=True
        ).distinct()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def create(self, request, *args, **kwargs):
        # Use custom serializer for creation
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
    """
    Account user management endpoints.
    """
    serializer_class = AccountUserSerializer
    permission_classes = [IsAuthenticated & IsBusinessOwner]
    
    def get_queryset(self):
        # Get account from business context
        business_id = self.kwargs.get('business_pk')
        if business_id:
            business = Business.objects.get(pk=business_id)
            return AccountUser.objects.filter(
                account=business.account
            )
        return AccountUser.objects.none()
```

### 5.3 Updated URL Configuration

**File:** `bizznexx_backend/urls.py` (updated)

```python
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from businesses.views import (
    BusinessViewSet,
    InquiryViewSet,
    LeadViewSet,
    MessageTemplateViewSet,
    PaymentViewSet,
    SetupProjectViewSet,
)
from businesses.views.auth import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    PasswordResetView,
)
from businesses.views.accounts import (
    AccountViewSet,
    AccountUserViewSet,
)

router = DefaultRouter()
router.register("businesses", BusinessViewSet, basename="business")
router.register("inquiries", InquiryViewSet, basename="inquiry")
router.register("leads", LeadViewSet, basename="lead")
router.register("payments", PaymentViewSet, basename="payment")
router.register("messages", MessageTemplateViewSet, basename="message-template")
router.register("setup-projects", SetupProjectViewSet, basename="setup-project")
router.register("accounts", AccountViewSet, basename="account")
router.register("account-users", AccountUserViewSet, basename="account-user")

# Public endpoints (no auth required)
public_router = DefaultRouter()


def health_check(request):
    return JsonResponse({"status": "ok", "service": "bizznexx-api"})


urlpatterns = [
    # Health check
    path("healthz", health_check),
    
    # Admin
    path("admin/", admin.site.urls),
    
    # API v1
    path("api/v1/", include([
        # Authentication
        path("auth/register/", UserRegistrationView.as_view({'post': 'register'}), name='register'),
        path("auth/login/", UserLoginView.as_view(), name='login'),
        path("auth/logout/", UserLogoutView.as_view({'post': 'logout'}), name='logout'),
        path("auth/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
        path("auth/me/", UserProfileView.as_view({'get': 'retrieve', 'patch': 'update'}), name='me'),
        path("auth/password/reset/", PasswordResetView.as_view({'post': 'request_reset'}), name='password_reset'),
        
        # Accounts
        path("accounts/", AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-list'),
        path("accounts/<int:pk>/", AccountViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='account-detail'),
        path("accounts/<int:pk>/invite/", AccountViewSet.as_view({'post': 'invite_user'}), name='account-invite'),
        path("accounts/<int:pk>/users/", AccountViewSet.as_view({'get': 'users'}), name='account-users'),
        
        # Businesses and other resources
        path("", include(router.urls)),
    ])),
    
    # Legacy API (for backward compatibility, deprecate later)
    path("api/", include(router.urls)),
]
```

---

## 6. Serializers

### 6.1 User Serializers

**File:** `businesses/serializers.py` (additions)

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


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
        
        # Validate password strength
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
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        if not User.objects.filter(email=value).exists():
            # Don't reveal if email exists or not
            return value
        
        return value
```

### 6.2 Account Serializers

**File:** `businesses/serializers.py` (additions)

```python
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
        
        # Make creating user the owner
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
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Check if user already exists
        user = User.objects.filter(email=value).first()
        if user:
            # Check if already in this account
            account = self.context['account']
            if AccountUser.objects.filter(user=user, account=account).exists():
                raise serializers.ValidationError(
                    "User already has access to this account."
                )
        
        return value
    
    def create(self, validated_data):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        account = self.context['account']
        request = self.context['request']
        
        email = validated_data['email']
        role = validated_data['role']
        
        # Check if user exists
        user = User.objects.filter(email=email).first()
        
        if user:
            # User exists, create account membership
            account_user = AccountUser.objects.create(
                user=user,
                account=account,
                role=role,
                invited_by=request.user,
                joined_at=timezone.now()  # Auto-join existing users
            )
            return account_user
        else:
            # User doesn't exist, create invitation
            # In production, send email invitation
            # For now, just create inactive membership
            account_user = AccountUser.objects.create(
                user=None,  # Will be set when user registers
                account=account,
                role=role,
                invited_by=request.user,
                is_active=False
            )
            return account_user
```

---

## 7. Migration Plan

### Step 1: Create User Model Migration

```bash
# Create migration for custom user model
python manage.py makemigrations businesses
```

### Step 2: Create Account Models Migration

```bash
# After adding Account, AccountUser models
python manage.py makemigrations businesses
```

### Step 3: Update Existing Business Model

```bash
# After adding account, created_by fields to Business
python manage.py makemigrations businesses
```

### Step 4: Create Superuser

```bash
python manage.py createsuperuser
# Use email as username
```

### Step 5: Migrate Existing Data

Create a data migration to:
1. Create accounts for existing businesses
2. Create users for existing business owners
3. Link everything together

---

## 8. Settings Updates

**File:** `bizznexx_backend/settings.py` (additions)

```python
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'businesses',
]

# Set custom user model
AUTH_USER_MODEL = 'businesses.User'

# JWT settings (as shown above)
SIMPLE_JWT = { ... }

# Update REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'businesses.permissions.TenantIsolationPermission',
    ),
}

# CORS settings for production
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://app.bizznexx.com",
    "https://www.bizznexx.com",
]

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    REFERRER_POLICY = 'same-origin'
```

---

## 9. Validation Checklist

- [x] Tenant isolation strategy decided
- [x] Account-Business-User relationship defined
- [x] User model designed
- [x] Account model designed
- [x] AccountUser model designed
- [x] Authentication method chosen (JWT)
- [x] Permission classes designed
- [x] API endpoints designed
- [x] Serializers designed
- [x] URL configuration designed
- [x] Settings updates identified
- [x] Migration plan outlined

## Next Steps

1. **Implement User model** - Create the custom user model
2. **Implement Account models** - Create Account and AccountUser models
3. **Update Business model** - Add account and created_by fields
4. **Create migrations** - Generate and apply database migrations
5. **Implement authentication views** - Create auth endpoints
6. **Implement account views** - Create account management endpoints
7. **Update permissions** - Implement tenant isolation
8. **Update frontend** - Add auth UI and account switching
9. **E-001:** Choose and implement auth approach (this document completes the choice)
10. **N-001:** Choose hosting architecture (can be done in parallel)
