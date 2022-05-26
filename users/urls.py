from django.urls import path
from django.contrib.auth import views as auth_views

import users.views as vws

app_name = 'users'

urlpatterns = [
    # profile stuff
    path('profile/', vws.profile, name='profile'),
    path('profile/edit/', vws.edit_profile, name='edit_profile'),

    # auth stuff
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('signup/', vws.signup, name='signup')
]
