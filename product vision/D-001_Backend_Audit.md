# D-001: Backend Architecture Audit

**Status:** Done  
**Owner:** BE  
**Priority:** P0  
**Date:** 2026-07-19

## Executive Summary

The backend is a **Django** application using **Django REST Framework (DRF)** with a **monolithic** structure. The data model is **well-designed** for the tutor/coaching domain with proper relationships. However, **critical production gaps** exist in authentication, authorization, tenant isolation, and deployment readiness.

**Verdict:** The backend models and API structure are **production-viable** but require **security hardening**, **tenant isolation**, and **operational improvements** before real user data is stored.

---

## 1. Current Architecture Overview

### Tech Stack

| Component | Technology | Status |
|-----------|------------|--------|
| Framework | Django | Current |
| REST API | Django REST Framework | Current |
| Database | SQLite (dev), PostgreSQL (prod-ready) | Configurable |
| ORM | Django ORM | Current |
| Auth | Django contrib.auth (unused) | Gap |
| CORS | django-cors-headers | Configured |
| Env Management | python-dotenv | Current |
| Deployment | Render (configured) | Ready |

### Project Structure

```
prototype/backend/
├── bizznexx_backend/
│   ├── __init__.py
│   ├── settings.py          # Django settings (87 lines)
│   ├── urls.py             # URL routing (32 lines)
│   ├── asgi.py
│   └── wsgi.py
├── businesses/
│   ├── __init__.py
│   ├── models.py           # Data models (288 lines)
│   ├── views.py            # API views (177 lines)
│   ├── serializers.py      # DRF serializers (160 lines)
│   ├── permissions.py      # Custom permissions (18 lines)
│   ├── personas.py          # Persona configurations (42 lines)
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       └── 0002_catalogueitem_details_catalogueitem_terms_and_more.py
├── db.sqlite3
└── manage.py
```

---

## 2. Settings Analysis (settings.py)

### Current Configuration

**Database:**
```python
DATABASE_URL = os.getenv("DATABASE_URL", "")
DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    if DATABASE_URL
    else {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```
**Strengths:**
- Supports both SQLite (dev) and PostgreSQL (prod)
- Connection pooling with `conn_max_age=600`
- Environment variable based

**Gaps:**
- No database connection health checks
- No migration validation in CI

**Security:**
```python
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-only-bizznexx-secret")
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = [host.strip() for host in os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",") if host.strip()]
BIZZNEXX_BETA_API_KEY = os.getenv("BIZZNEXX_BETA_API_KEY", "")
```
**Strengths:**
- Environment variable based
- Debug mode configurable

**Critical Gaps:**
- `DEBUG=True` in production is **DANGEROUS** (exposes sensitive data)
- `ALLOWED_HOSTS=["*"]` is **DANGEROUS** (allows any host)
- Default SECRET_KEY is **INSECURE** (must be unique per deployment)
- No HTTPS enforcement
- No security headers (HSTS, X-Frame-Options, etc.)

**CORS:**
```python
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", str(DEBUG)).lower() == "true"
CORS_ALLOWED_ORIGINS = [
    origin.strip() for origin in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if origin.strip()
]
```
**Gaps:**
- `CORS_ALLOW_ALL_ORIGINS=True` in dev is fine
- No explicit production CORS configuration
- Should restrict to frontend domains in production

**API:**
```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["businesses.permissions.BetaApiKeyPermission"],
}
```
**Strengths:**
- Custom permission class applied globally
- API key based access control

**Gaps:**
- No authentication classes
- No rate limiting
- No throttling

---

## 3. Data Model Analysis (businesses/models.py)

### Model Inventory

| Model | Purpose | Relationships | Status |
|-------|---------|---------------|--------|
| `Business` | Business/tenant root | OneToOne: Catalogue, SetupProject | Core |
| `SetupProject` | Operator setup workflow | OneToOne: Business | Core |
| `Catalogue` | Business service catalogue | OneToOne: Business, ForeignKey: CatalogueItem | Core |
| `CatalogueItem` | Individual service/offering | ForeignKey: Catalogue | Core |
| `TrustProof` | Proof/testimonial items | ForeignKey: Business | Core |
| `FAQ` | Frequently asked questions | ForeignKey: Catalogue | Core |
| `MediaAsset` | Images/videos | ForeignKey: Business | Core |
| `Testimonial` | Customer testimonials | ForeignKey: Business | Core |
| `CaseStudy` | Case studies | ForeignKey: Business | Core |
| `PageEvent` | Analytics events | ForeignKey: Business, CatalogueItem | Core |
| `Inquiry` | Parent/student inquiry | ForeignKey: Business, CatalogueItem | Core |
| `Lead` | Sales lead | ForeignKey: Business, Inquiry | Core |
| `FollowUpTask` | Action items | ForeignKey: Business, Lead | Core |
| `Customer` | Enrolled student/client | ForeignKey: Business, Lead | Core |
| `Payment` | Fee/payment tracking | ForeignKey: Business, Customer, Lead | Core |
| `MessageTemplate` | WhatsApp message templates | ForeignKey: Business | Core |
| `ScoreSnapshot` | Historical scores | ForeignKey: Business | Core |
| `ScoreReason` | Score explanation | ForeignKey: Business | Core |
| `OperatorNote` | Internal notes | ForeignKey: Business | Core |

### Model Field Analysis

#### Business Model (Lines 4-28)

**Fields:**
- `name` - CharField(160) - Business name
- `owner_name` - CharField(120) - Owner name
- `persona_pack` - CharField(40) with choices - TUTOR, EVENT, AGENCY, CONSULTANT, CREATOR, HOME_SERVICE
- `city` - CharField(80) - Location
- `whatsapp_number` - CharField(32) - Contact number
- `public_slug` - SlugField(unique=True) - URL slug
- `preferred_language` - CharField(40, default="Hinglish")
- `brand_tone` - CharField(80, default="Friendly professional")
- `payment_terms` - TextField(blank=True)
- `growth_score` - PositiveSmallIntegerField(default=0)
- `health_score` - PositiveSmallIntegerField(default=0)
- `created_at` - DateTimeField(auto_now_add=True)
- `updated_at` - DateTimeField(auto_now=True)

**Strengths:**
- Good field coverage for tutor business
- Persona pack supports multiple business types
- Timestamps for auditing

**Gaps:**
- No user/account relationship (tenant isolation gap)
- No authentication fields (email, password hash)
- No soft delete field
- No custom validation

#### SetupProject Model (Lines 31-47)

**Fields:**
- `business` - OneToOneField(Business) - Related business
- `stage` - CharField(40) with choices - INTAKE, CATALOGUE_DRAFT, PAGE_REVIEW, PUBLISHED, WEEKLY_REVIEW
- `package_name` - CharField(80, default="Starter Pilot")
- `owner_inputs_complete` - BooleanField(default=False)
- `blockers` - TextField(blank=True)
- `target_publish_date` - DateField(null=True, blank=True)

**Strengths:**
- Good operator workflow tracking
- Clear stage definitions

**Gaps:**
- No operator assignment
- No timestamps

#### Catalogue & CatalogueItem Models (Lines 50-78)

**Strengths:**
- OneToOne relationship between Business and Catalogue
- CatalogueItem has display_order for sorting
- Price as label (supports flexible pricing display)
- Rich description fields

**Gaps:**
- No currency field (assumes INR)
- No pricing validation

#### Inquiry Model (Lines 161-175)

**Fields:**
- `business` - ForeignKey(Business)
- `catalogue_item` - ForeignKey(CatalogueItem, null=True)
- `name` - CharField(120) - Parent/student name
- `phone_number` - CharField(32)
- `message` - TextField(blank=True)
- `source` - CharField(80, default="public_page")
- `extra_context` - JSONField(default=dict, blank=True) - **Persona-specific fields**
- `is_qualified` - BooleanField(default=False)
- `created_at` - DateTimeField(auto_now_add=True)

**Strengths:**
- JSONField for flexible persona-specific data
- Source tracking for analytics
- Qualification flag

**Gaps:**
- No consent timestamp (E-006 requirement)
- No privacy flags
- No data retention policy field

#### Lead Model (Lines 178-196)

**Fields:**
- `business` - ForeignKey(Business)
- `inquiry` - OneToOneField(Inquiry, null=True) - Links to inquiry
- `name` - CharField(120)
- `phone_number` - CharField(32)
- `interested_service` - CharField(140)
- `source` - CharField(80)
- `status` - CharField(80) - **Persona-specific statuses**
- `expected_value` - DecimalField(10,2, default=0)
- `next_action` - CharField(220, blank=True)
- `follow_up_age_days` - PositiveSmallIntegerField(default=0)
- `urgency_reason` - CharField(220, blank=True)
- `next_follow_up_date` - DateField(null=True, blank=True)
- `notes` - TextField(blank=True)
- `created_at` - DateTimeField(auto_now_add=True)
- `updated_at` - DateTimeField(auto_now=True)

**Strengths:**
- Rich lead tracking fields
- Status and next_action for workflow
- Urgency tracking
- Timestamps for auditing

**Gaps:**
- No status choices/validation (D-006 requirement)
- No tenant isolation (D-002 requirement)
- No assignment to specific user

#### Payment Model (Lines 224-246)

**Fields:**
- `Status` - TextChoices: UNPAID, PART_PAID, PAID, OVERDUE
- `business` - ForeignKey(Business)
- `customer` - ForeignKey(Customer, null=True)
- `lead` - ForeignKey(Lead, null=True)
- `payer_name` - CharField(120)
- `service_name` - CharField(140)
- `amount_due` - DecimalField(10,2)
- `amount_paid` - DecimalField(10,2, default=0)
- `due_date` - DateField(null=True, blank=True)
- `status` - CharField(32, choices=Status.choices, default=Status.UNPAID)
- `age_days` - PositiveSmallIntegerField(default=0)
- `urgency_reason` - CharField(220, blank=True)
- `payment_mode` - CharField(60, blank=True)
- `reference_note` - CharField(180, blank=True)

**Strengths:**
- Clear status choices
- Supports partial payments
- Age tracking for overdue
- Multiple relationship options (customer or lead)

**Gaps:**
- No payment date
- No receipt/invoice number
- No tax fields

#### Customer Model (Lines 212-221)

**Fields:**
- `business` - ForeignKey(Business)
- `lead` - OneToOneField(Lead, null=True)
- `name` - CharField(120)
- `phone_number` - CharField(32, blank=True)
- `active_status` - CharField(40, default="active")
- `start_date` - DateField(null=True, blank=True)

**Strengths:**
- Links to lead for history
- Active status tracking

**Gaps:**
- No end date
- No relationship to payments (goes through lead)
- No contact preferences

---

## 4. API Analysis (businesses/views.py)

### ViewSet Inventory

| ViewSet | Model | Endpoints | Custom Actions |
|---------|-------|-----------|----------------|
| `BusinessViewSet` | Business | GET, POST, PATCH, DELETE | `page_event`, `summary` |
| `InquiryViewSet` | Inquiry | GET, POST, PATCH, DELETE | `capture` |
| `LeadViewSet` | Lead | GET, POST, PATCH, DELETE | `set_status`, `suggested_message` |
| `PaymentViewSet` | Payment | GET, POST, PATCH, DELETE | `mark_paid`, `reminder` |
| `MessageTemplateViewSet` | MessageTemplate | GET, POST, PATCH, DELETE | None |
| `SetupProjectViewSet` | SetupProject | GET, POST, PATCH, DELETE | None |
| `PageEventViewSet` | PageEvent | GET, POST, PATCH, DELETE | None |

### Custom Actions

#### InquiryViewSet.capture (Lines 70-116)

**Purpose:** Create inquiry and automatically create lead + follow-up task

**Workflow:**
1. Validates `PublicInquirySerializer`
2. Creates `Inquiry` record
3. Creates `Lead` record with persona-specific first status and action
4. Creates `FollowUpTask` with suggested message
5. Logs `PageEvent` for analytics
6. Returns both inquiry and lead data

**Strengths:**
- Atomic operation (all or nothing)
- Persona-aware (uses PERSONA_PACKS)
- Automatic task creation
- Analytics tracking

**Gaps:**
- No consent capture (E-006)
- No duplicate detection
- No rate limiting

#### LeadViewSet.set_status (Lines 123-129)

**Purpose:** Update lead status and next action

**Strengths:**
- Simple and focused
- Only updates specified fields

**Gaps:**
- No validation against persona-specific statuses (D-006)
- No audit logging

#### LeadViewSet.suggested_message (Lines 131-136)

**Purpose:** Generate WhatsApp message template for lead

**Strengths:**
- Persona-aware template filling
- Uses `fill_template` from personas.py

**Gaps:**
- None significant

#### PaymentViewSet.mark_paid (Lines 143-150)

**Purpose:** Mark payment as paid

**Strengths:**
- Updates amount_paid if provided
- Defaults to full amount

**Gaps:**
- No receipt generation
- No notification triggering

#### PaymentViewSet.reminder (Lines 152-162)

**Purpose:** Generate payment reminder message

**Strengths:**
- Persona-aware template filling
- Proper amount formatting

**Gaps:**
- None significant

#### BusinessViewSet.summary (Lines 50-63)

**Purpose:** Get business dashboard summary

**Returns:**
- open_leads count
- follow_ups count
- pending_amount sum
- page_views count
- whatsapp_clicks count
- growth_score
- health_score

**Strengths:**
- Single query for dashboard data
- Aggregated metrics

**Gaps:**
- No caching
- Some queries could be optimized

---

## 5. Serializer Analysis (businesses/serializers.py)

### Serializer Inventory

| Serializer | Model | Purpose |
|-----------|-------|---------|
| `BusinessSerializer` | Business | Full business with nested relations |
| `CatalogueSerializer` | Catalogue | Catalogue with items and FAQs |
| `CatalogueItemSerializer` | CatalogueItem | Individual catalogue item |
| `TrustProofSerializer` | TrustProof | Trust proof item |
| `FAQSerializer` | FAQ | FAQ item |
| `MediaAssetSerializer` | MediaAsset | Media asset |
| `TestimonialSerializer` | Testimonial | Testimonial |
| `CaseStudySerializer` | CaseStudy | Case study |
| `SetupProjectSerializer` | SetupProject | Setup project |
| `LeadSerializer` | Lead | Lead data |
| `PaymentSerializer` | Payment | Payment data |
| `FollowUpTaskSerializer` | FollowUpTask | Task data |
| `MessageTemplateSerializer` | MessageTemplate | Message template |
| `ScoreReasonSerializer` | ScoreReason | Score reason |
| `OperatorNoteSerializer` | OperatorNote | Operator note |
| `InquirySerializer` | Inquiry | Inquiry data |
| `PublicInquirySerializer` | None | Inquiry creation (write-only) |
| `PageEventSerializer` | PageEvent | Page event |

### BusinessSerializer (Lines 111-136)

**Nested Fields:**
- `catalogue` - CatalogueSerializer (read_only)
- `trust_proof` - TrustProofSerializer (many, read_only)
- `media_assets` - MediaAssetSerializer (many, read_only)
- `testimonials` - TestimonialSerializer (many, read_only)
- `case_studies` - CaseStudySerializer (many, read_only)
- `setup_project` - SetupProjectSerializer (read_only)
- `leads` - LeadSerializer (many, read_only)
- `payments` - PaymentSerializer (many, read_only)
- `tasks` - FollowUpTaskSerializer (many, read_only)
- `message_templates` - MessageTemplateSerializer (many, read_only)
- `score_reasons` - ScoreReasonSerializer (many, read_only)
- `operator_notes` - OperatorNoteSerializer (many, read_only)
- `page_views` - SerializerMethodField
- `whatsapp_clicks` - SerializerMethodField

**Strengths:**
- Comprehensive nested serialization
- Computed fields for analytics
- Read-only nested to prevent accidental updates

**Gaps:**
- No pagination for nested lists
- No filtering for nested lists
- Could be performance issue with many nested items

---

## 6. Persona System Analysis (businesses/personas.py)

### PERSONA_PACKS Structure

```python
PERSONA_PACKS = {
    "tutor": {
        "label": "Tutor / Coach",
        "statuses": [...],
        "first_status": "...",
        "first_action": "...",
        "messages": {...}
    },
    # ... other personas
}
```

**Strengths:**
- Centralized persona configurations
- Easy to extend with new personas
- Used throughout views and frontend
- Supports persona-specific workflows

**Gaps:**
- Hardcoded in Python (not database-backed)
- No validation that persona_pack values match
- No versioning for persona packs

### fill_template Function (Lines 38-41)

**Purpose:** Replace template variables with provided values

**Strengths:**
- Simple string replacement
- Handles missing values gracefully

**Gaps:**
- No template syntax validation
- No escaping for special characters

---

## 7. Permission System Analysis (businesses/permissions.py)

### BetaApiKeyPermission (Lines 5-17)

**Purpose:** Optional API key gate for private deployments

**Logic:**
- If `BIZZNEXX_BETA_API_KEY` is unset: allow all
- If set: require `X-BizzNexx-Beta-Key` header to match

**Strengths:**
- Simple implementation
- Optional (dev-friendly)
- Environment configurable

**Gaps:**
- **No authentication** (only API key, not user-based)
- **No tenant isolation** (API key applies to all businesses)
- **No rate limiting**
- **No user identification**
- No granular permissions (all or nothing)

---

## 8. URL Routing Analysis (bizznexx_backend/urls.py)

### Current Routes

```python
urlpatterns = [
    path("healthz", health_check),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
```

**DRF Router Routes:**
- `/api/businesses/` - Business CRUD + summary, page_event
- `/api/inquiries/` - Inquiry CRUD + capture
- `/api/leads/` - Lead CRUD + set_status, suggested_message
- `/api/payments/` - Payment CRUD + mark_paid, reminder
- `/api/messages/` - MessageTemplate CRUD
- `/api/setup-projects/` - SetupProject CRUD

**Strengths:**
- RESTful conventions
- Consistent naming
- Custom actions for workflows

**Gaps:**
- No versioning (`/api/v1/`)
- No authentication endpoints
- No public page endpoints (for non-auth users)
- No health check details

---

## 9. Production Readiness Analysis

### Critical Gaps (Must Fix Before Production)

| ID | Issue | Priority | Effort | Dependencies |
|----|-------|----------|--------|--------------|
| BE-001 | No user authentication | P0 | High | None |
| BE-002 | No tenant isolation | P0 | High | D-002 |
| BE-003 | No authorization | P0 | High | BE-001 |
| BE-004 | Insecure default settings | P0 | Low | None |
| BE-005 | No rate limiting | P0 | Medium | None |
| BE-006 | No audit logging | P0 | Medium | None |
| BE-007 | No data backup | P0 | Medium | N-001 |
| BE-008 | No monitoring | P0 | Medium | N-001 |
| BE-009 | No HTTPS enforcement | P0 | Low | None |
| BE-010 | No security headers | P0 | Low | None |

### Recommended Gaps (Should Fix Before Production)

| ID | Issue | Priority | Effort | Dependencies |
|----|-------|----------|--------|--------------|
| BE-011 | No API versioning | P1 | Low | None |
| BE-012 | No OpenAPI/Swagger docs | P1 | Low | None |
| BE-013 | No request validation | P1 | Medium | None |
| BE-014 | No soft delete | P1 | Medium | None |
| BE-015 | No caching | P1 | Medium | None |
| BE-016 | No database indexes | P1 | Medium | None |

---

## 10. Data Model Gaps for Production

### D-002: Tenant/Account Model

**Current State:** No user model, no account model. Businesses are standalone.

**Required:**
1. **User model** - Django's built-in auth.User or custom
2. **Account model** - For multi-business owners
3. **Business-User relationship** - ManyToMany or ForeignKey
4. **Role system** - Owner, Operator, Admin

**Recommended Implementation:**
```python
class User(AbstractUser):
    phone_number = models.CharField(max_length=32, blank=True)
    preferred_language = models.CharField(max_length=40, default="en")
    
class Account(models.Model):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Business(models.Model):
    # ... existing fields
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
```

### D-004: Course/Batch/Program Model

**Current State:** `CatalogueItem` serves as course/batch/program.

**Gaps:**
- No batch scheduling (start date, end date, frequency)
- No capacity tracking
- No enrollment tracking per batch
- No session tracking

**Recommended:** Extend `CatalogueItem` or create separate `Batch` model.

### D-005: Inquiry Model Enhancements

**Current State:** Basic inquiry capture.

**Required for E-006 (Consent):**
```python
class Inquiry(models.Model):
    # ... existing fields
    consent_version = models.CharField(max_length=40, default="v1")
    consent_timestamp = models.DateTimeField(null=True, blank=True)
    consent_ip = models.GenericIPAddressField(null=True, blank=True)
    privacy_policy_accepted = models.BooleanField(default=False)
```

### D-006: Lead/Trial States

**Current State:** Free-form status field.

**Required:**
1. Define status choices per persona
2. Add validation in serializer
3. Add state transition rules

**Recommended:**
```python
class Lead(models.Model):
    # ... existing fields
    
    class Status(models.TextChoices):
        NEW_INQUIRY = "new_inquiry", "New inquiry"
        TRIAL_OPTIONS_SENT = "trial_options_sent", "Trial options sent"
        TRIAL_SCHEDULED = "trial_scheduled", "Trial scheduled"
        TRIAL_COMPLETED = "trial_completed", "Trial completed"
        FEE_PLAN_SENT = "fee_plan_sent", "Fee plan sent"
        ENROLLED = "enrolled", "Enrolled"
        LOST = "lost", "Lost"
    
    status = models.CharField(max_length=80, choices=Status.choices)
```

---

## 11. API Gaps for Production

### Missing Endpoints

| Endpoint | Purpose | Priority |
|----------|---------|----------|
| `/api/auth/login/` | User login | P0 |
| `/api/auth/logout/` | User logout | P0 |
| `/api/auth/me/` | Current user info | P0 |
| `/api/auth/refresh/` | Token refresh | P0 |
| `/api/businesses/{slug}/` | Public business page (no auth) | P0 |
| `/api/businesses/{slug}/inquiries/` | Public inquiry submission | P0 |
| `/api/v1/...` | Versioned API | P1 |

### Missing Features

| Feature | Purpose | Priority |
|---------|---------|----------|
| Rate limiting | Prevent abuse | P0 |
| Request logging | Debugging and audit | P0 |
| Error tracking | Sentry/rollbar integration | P0 |
| API documentation | Swagger/OpenAPI | P1 |
| Webhooks | WhatsApp integration | P1 |

---

## 12. Security Hardening Requirements

### Immediate Fixes

1. **Settings Override for Production:**
```python
# In production settings file
DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")  # Must be set
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ["https://yourdomain.com", "https://www.yourdomain.com"]
CSRF_TRUSTED_ORIGINS = ["https://yourdomain.com", "https://www.yourdomain.com"]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

2. **Security Headers:**
```python
# Add to middleware or settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "same-origin"
```

3. **Database Security:**
- Use PostgreSQL in production (not SQLite)
- Encrypt sensitive fields at rest
- Regular backups with encryption

---

## 13. Refactoring Recommendations

### Phase 1: Foundation (Before Any New Features)

1. **D-002: Define tenant/account model**
   - Add User model (extend AbstractUser)
   - Add Account model
   - Add Business-Account-User relationships
   - Create migrations

2. **E-001: Implement authentication**
   - Choose approach: Django REST Framework SimpleJWT recommended
   - Add login/logout endpoints
   - Add token refresh
   - Add user serialization

3. **Add authorization**
   - Object-level permissions
   - Tenant isolation middleware
   - Role-based access control

4. **Fix security settings**
   - Create production settings file
   - Set secure defaults
   - Add environment validation

### Phase 2: Production Hardening

5. **Add rate limiting**
   - Use django-ratelimit or DRF throttling
   - Configure per-endpoint limits

6. **Add audit logging**
   - Log sensitive operations
   - Track data changes
   - Store audit trail

7. **Add request logging**
   - Log all API requests
   - Include user, timestamp, endpoint, status
   - Retention policy

8. **Add monitoring**
   - Health check endpoint enhancements
   - Prometheus metrics
   - Error tracking (Sentry)

### Phase 3: Quality Improvements

9. **Add API versioning**
   - Version prefixes (`/api/v1/`)
   - Deprecation policy
   - Migration path

10. **Add OpenAPI documentation**
    - Use drf-spectacular or drf-yasg
    - Auto-generate from code
    - Keep in sync with frontend

11. **Add caching**
    - Cache business summaries
    - Cache public pages
    - Invalidate on changes

12. **Add database indexes**
    - Index frequently queried fields
    - Analyze query performance
    - Add migration for indexes

---

## 14. Validation Checklist

- [x] Tech stack documented
- [x] Settings analyzed
- [x] Data models inventoried
- [x] API endpoints documented
- [x] Serializers documented
- [x] Permission system analyzed
- [x] Persona system analyzed
- [x] Critical gaps identified
- [x] Recommended gaps identified
- [x] Refactoring recommendations provided
- [x] Security requirements documented
- [x] Tenant model requirements defined
- [x] Auth requirements defined

## Next Steps

1. **D-002:** Define and implement tenant/account model
2. **E-001:** Choose and implement auth approach (parallel)
3. **N-001:** Choose hosting architecture (parallel)
4. **D-004:** Define Course/Batch/Program model
5. **D-005:** Enhance Inquiry model with consent fields
6. **D-006:** Define Lead status choices and validation
7. Create production settings override
8. Implement security hardening
