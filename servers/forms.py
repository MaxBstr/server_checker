import re

from django import forms
from django.core.exceptions import ValidationError

from servers.models import Server


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
