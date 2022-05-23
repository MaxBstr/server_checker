import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from servers.models import UserProfile, Server


class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'work_position', 'email', 'username']


class ServerCreateOrUpdateForm(forms.ModelForm):
    ip = forms.CharField(max_length=15)

    class Meta:
        model = Server
        fields = ['ip', 'name']

    def clean_ip(self):
        ip = self.cleaned_data['ip']
        digit_pattern = r'\d{1,3}.'
        pattern: str = digit_pattern * 4

        if not re.match(pattern[:-1], ip):
            raise ValidationError("ip format is incorrect")
        return ip


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('first_name', 'middle_name', 'last_name', 'work_position', 'username', 'email')
