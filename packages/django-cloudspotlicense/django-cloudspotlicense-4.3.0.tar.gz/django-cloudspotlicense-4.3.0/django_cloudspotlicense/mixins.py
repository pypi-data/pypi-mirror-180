from django.contrib.auth.mixins import PermissionRequiredMixin as django_PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django_cloudspotlicense import PACKAGE_NAME
from django.shortcuts import redirect
from django.contrib.auth import logout

class PermissionRequiredMixin(django_PermissionRequiredMixin):
    """ Verify that the current user has all specified permissions on the Cloudspot License server. """
    
    def get_permission_required(self):
        if self.permission_required is None:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} is missing the "
                f"permission_required attribute. Define "
                f"{self.__class__.__name__}.permission_required, or override "
                f"{self.__class__.__name__}.get_permission_required()."
            )
            
        if isinstance(self.permission_required, str):
            permission_required = '{0}.{1}'.format(PACKAGE_NAME, self.permission_required)
            perms = (permission_required,)
        else:
            perms = []
            for perm in self.permission_required:
                perms.append(
                    '{0}.{1}'.format(PACKAGE_NAME, perm)
                )
        
        return perms
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not request.user.company:
            if request.user.available_companies.count() > 0:
                return redirect('select_company')
            else:
                logout(request)
        
        return super().dispatch(request, *args, **kwargs)