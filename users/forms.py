from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Имя пользователя')
    first_name = forms.CharField(max_length=20, label='Имя')
    middle_name = forms.CharField(max_length=40, label='Отчество')
    last_name = forms.CharField(max_length=60, label='Фамилия')
    work_position = forms.CharField(max_length=100, label='Должность')
    email = forms.EmailField(label='Почта')

    class Meta:
        model = UserProfile
        fields = (
            'last_name', 'first_name', 'middle_name',
            'work_position', 'email', 'username'
        )


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя')
    first_name = forms.CharField(max_length=20, label='Имя')
    middle_name = forms.CharField(max_length=40, label='Отчество')
    last_name = forms.CharField(max_length=60, label='Фамилия')
    work_position = forms.CharField(max_length=100, label='Должность')
    email = forms.EmailField(label='Почта')

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields + (
            'last_name', 'first_name', 'middle_name',
            'work_position', 'username', 'email'
        )
