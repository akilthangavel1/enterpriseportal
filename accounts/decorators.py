from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse


def _redirect_to_role_dashboard(user):
    if user.is_superuser or user.is_admin:
        return redirect(reverse("dashboards:admin"))
    if user.is_approved and user.role == "faculty":
        return redirect(reverse("dashboards:faculty"))
    if user.is_approved and user.role == "hod":
        return redirect(reverse("dashboards:hod"))
    if user.is_approved and user.role == "principal":
        return redirect(reverse("dashboards:principal"))
    return redirect(reverse("dashboards:student"))


def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect(reverse("accounts:login"))
            if user.is_admin or user.is_superuser:
                return view_func(request, *args, **kwargs)
            if user.role in allowed_roles and user.is_approved:
                return view_func(request, *args, **kwargs)
            return _redirect_to_role_dashboard(user)

        return _wrapped_view

    return decorator


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse("accounts:login"))
        if user.is_admin or user.is_superuser:
            return view_func(request, *args, **kwargs)
        return _redirect_to_role_dashboard(user)

    return _wrapped_view
