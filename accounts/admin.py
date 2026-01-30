from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "role",
        "is_approved",
        "is_active",
        "is_staff",
    )
    list_filter = ("role", "is_approved", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Portal Role", {"fields": ("role", "is_approved", "is_faculty", "is_hod", "is_principal", "is_admin")}),
    )

    actions = [
        "approve_users",
        "disable_users",
        "enable_users",
        "set_role_student",
        "set_role_faculty",
        "set_role_hod",
        "set_role_principal",
        "set_role_admin",
    ]

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)

    def disable_users(self, request, queryset):
        queryset.update(is_active=False)

    def enable_users(self, request, queryset):
        queryset.update(is_active=True)

    def _set_role(self, queryset, role):
        queryset.update(role=role, is_approved=True)

    def set_role_student(self, request, queryset):
        self._set_role(queryset, User.ROLE_STUDENT)

    def set_role_faculty(self, request, queryset):
        self._set_role(queryset, User.ROLE_FACULTY)

    def set_role_hod(self, request, queryset):
        self._set_role(queryset, User.ROLE_HOD)

    def set_role_principal(self, request, queryset):
        self._set_role(queryset, User.ROLE_PRINCIPAL)

    def set_role_admin(self, request, queryset):
        self._set_role(queryset, User.ROLE_ADMIN)
