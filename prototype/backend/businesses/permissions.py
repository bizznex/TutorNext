from django.conf import settings
from rest_framework import permissions
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


class IsAuthenticatedOrBetaKey(BasePermission):
    """
    Allows access if:
    1. User is authenticated (JWT), OR
    2. Valid beta API key is provided (for public pages)
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        
        expected_key = getattr(settings, "BIZZNEXX_BETA_API_KEY", "")
        if not expected_key:
            return True
        return request.headers.get("X-BizzNexx-Beta-Key") == expected_key


class IsBusinessOwner(BasePermission):
    """
    Check if user is owner/admin of the business.
    """

    def has_object_permission(self, request, view, obj):
        from .models import Business, AccountUser
        
        if not request.user or not request.user.is_authenticated:
            return False
        
        business = obj if isinstance(obj, Business) else getattr(obj, 'business', None)
        if not business:
            return False
        
        account_user = AccountUser.objects.filter(
            user=request.user,
            account=business.account,
            is_active=True
        ).first()
        
        if not account_user:
            return False
        
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
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
            if request.user and request.user.is_authenticated:
                from .models import AccountUser, Business
                account_ids = AccountUser.objects.filter(
                    user=request.user,
                    is_active=True
                ).values_list('account_id', flat=True)
                
                business_ids = Business.objects.filter(
                    account_id__in=account_ids
                ).values_list('id', flat=True)
                
                if hasattr(queryset, 'filter'):
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

