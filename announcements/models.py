from django.db import models
from django.conf import settings

class Announcement(models.Model):
    DEPARTMENT_CHOICES = [
        ('ALL', 'All Departments'),
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics & Communication'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('IT', 'Information Technology'),
        ('MBA', 'Management Studies'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='ALL')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
