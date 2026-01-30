from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LoginForm, ProfileForm, RegistrationForm
from .models import User


def _redirect_to_role_dashboard(user):
    if user.is_superuser or user.is_admin:
        return redirect(reverse("dashboards:admin"))
    if user.is_approved and user.role == User.ROLE_FACULTY:
        return redirect(reverse("dashboards:faculty"))
    if user.is_approved and user.role == User.ROLE_HOD:
        return redirect(reverse("dashboards:hod"))
    if user.is_approved and user.role == User.ROLE_PRINCIPAL:
        return redirect(reverse("dashboards:principal"))
    return redirect(reverse("dashboards:student"))


def register_view(request):
    if request.user.is_authenticated:
        return _redirect_to_role_dashboard(request.user)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("accounts:login"))
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return _redirect_to_role_dashboard(request.user)
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return _redirect_to_role_dashboard(user)
    else:
        form = LoginForm(request)
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("accounts:login"))


@login_required
def profile_view(request):
    return render(request, "profile_view.html")


@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse("accounts:profile"))
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "profile.html", {"form": form})
