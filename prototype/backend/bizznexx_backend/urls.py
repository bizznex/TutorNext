from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from businesses.views import (
    BusinessViewSet,
    InquiryViewSet,
    LeadViewSet,
    MessageTemplateViewSet,
    PaymentViewSet,
    SetupProjectViewSet,
)

router = DefaultRouter()
router.register("businesses", BusinessViewSet, basename="business")
router.register("inquiries", InquiryViewSet, basename="inquiry")
router.register("leads", LeadViewSet, basename="lead")
router.register("payments", PaymentViewSet, basename="payment")
router.register("messages", MessageTemplateViewSet, basename="message-template")
router.register("setup-projects", SetupProjectViewSet, basename="setup-project")


def health_check(request):
    return JsonResponse({"status": "ok", "service": "bizznexx-beta-api"})


urlpatterns = [
    path("healthz", health_check),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
