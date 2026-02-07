from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Announcement
from .forms import AnnouncementForm

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if user can create (everyone except students)
        context['can_create'] = self.request.user.role != 'student'
        return context

class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcement_list')

    def test_func(self):
        # Allow everyone except students
        return self.request.user.role != 'student'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
