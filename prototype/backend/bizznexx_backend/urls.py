from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from businesses.views import (
    AccountViewSet,
    AccountUserViewSet,
    BusinessViewSet,
    InquiryViewSet,
    LeadViewSet,
    MessageTemplateViewSet,
    PageEventViewSet,
    PaymentViewSet,
    SetupProjectViewSet,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserRegistrationView,
    PasswordResetView,
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


def health_check(request):
    return JsonResponse({"status": "ok", "service": "bizznexx-api"})


urlpatterns = [
    path("healthz", health_check),
    path("admin/", admin.site.urls),
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
