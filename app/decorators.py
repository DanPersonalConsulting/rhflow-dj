from django.core.exceptions import PermissionDenied
from functools import wraps

def org_admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_org_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
