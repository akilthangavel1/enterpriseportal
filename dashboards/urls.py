from django.urls import path
from . import views


app_name = "dashboards"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.student_dashboard, name="student"),
    path("dashboard/faculty/", views.faculty_dashboard, name="faculty"),
    path("dashboard/hod/", views.hod_dashboard, name="hod"),
    path("dashboard/principal/", views.principal_dashboard, name="principal"),
    path("dashboard/admin/", views.admin_dashboard, name="admin"),
]
