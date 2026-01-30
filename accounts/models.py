from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_STUDENT = "student"
    ROLE_FACULTY = "faculty"
    ROLE_HOD = "hod"
    ROLE_PRINCIPAL = "principal"
    ROLE_ADMIN = "admin"

    ROLE_CHOICES = [
        (ROLE_STUDENT, "Student"),
        (ROLE_FACULTY, "Faculty"),
        (ROLE_HOD, "HOD"),
        (ROLE_PRINCIPAL, "Principal"),
        (ROLE_ADMIN, "Admin"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_STUDENT)
    is_faculty = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def set_role_flags(self):
        self.is_faculty = self.role == self.ROLE_FACULTY
        self.is_hod = self.role == self.ROLE_HOD
        self.is_principal = self.role == self.ROLE_PRINCIPAL
        self.is_admin = self.role == self.ROLE_ADMIN

    def save(self, *args, **kwargs):
        self.set_role_flags()
        super().save(*args, **kwargs)
