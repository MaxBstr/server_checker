import re

from django import forms
from django.core.exceptions import ValidationError

from servers.models import Server


class ServerCreateOrUpdateForm(forms.ModelForm):
    ip = forms.CharField(max_length=20)

    class Meta:
        model = Server
        fields = ['ip', 'name']

    def clean_ip(self):
        ip = self.cleaned_data['ip']
        ip_pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'

        if not re.match(ip_pattern, ip):
            raise ValidationError("ip format is incorrect")
        return ip
