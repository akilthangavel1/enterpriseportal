from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.decorators import admin_required, role_required
from accounts.models import User


def home(request):
    if request.user.is_authenticated:
        user = request.user
        if user.is_superuser or user.is_admin:
            return redirect(reverse("dashboards:admin"))
        if user.is_approved and user.role == User.ROLE_FACULTY:
            return redirect(reverse("dashboards:faculty"))
        if user.is_approved and user.role == User.ROLE_HOD:
            return redirect(reverse("dashboards:hod"))
        if user.is_approved and user.role == User.ROLE_PRINCIPAL:
            return redirect(reverse("dashboards:principal"))
        return redirect(reverse("dashboards:student"))
    return render(request, "home.html")


@login_required
def student_dashboard(request):
    return render(request, "dashboards/student.html")


@role_required([User.ROLE_FACULTY])
def faculty_dashboard(request):
    return render(request, "dashboards/faculty.html")


@role_required([User.ROLE_HOD])
def hod_dashboard(request):
    return render(request, "dashboards/hod.html")


@role_required([User.ROLE_PRINCIPAL])
def principal_dashboard(request):
    return render(request, "dashboards/principal.html")


@admin_required
def admin_dashboard(request):
    return render(request, "dashboards/admin.html")
