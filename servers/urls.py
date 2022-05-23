from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

import servers.views as vws

app_name = 'servers'

actions_list = {'post': 'create', 'patch': 'update', 'delete': 'destroy'}

urlpatterns = [
    path('', vws.index, name='index'),
    path('profile/', vws.profile, name='profile'),
    path('profile/edit/', vws.edit_profile, name='edit_profile'),
    path('server/', vws.create_or_update_server, name='server'),

    path('register/', vws.register, name='register'),
    path('logout/', vws.logout_user, name='logout')
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
