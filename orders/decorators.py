from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login_view_url')  # Redirect to login if not authenticated
            
            if request.user.role not in roles:
                raise PermissionDenied("Access denied.")  # Raise 403 if authenticated but wrong role
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator