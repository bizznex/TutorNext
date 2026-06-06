from django.conf import settings
from rest_framework.permissions import BasePermission


class BetaApiKeyPermission(BasePermission):
    """
    Optional beta gate for private deployments.

    If BIZZNEXX_BETA_API_KEY is unset, local/dev behavior stays open.
    If set, API callers must send X-BizzNexx-Beta-Key with the same value.
    """

    def has_permission(self, request, view):
        expected_key = getattr(settings, "BIZZNEXX_BETA_API_KEY", "")
        if not expected_key:
            return True
        return request.headers.get("X-BizzNexx-Beta-Key") == expected_key

