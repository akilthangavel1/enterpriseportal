from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'department', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter announcement title'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 6, 'placeholder': 'Enter announcement details...'}),
        }
