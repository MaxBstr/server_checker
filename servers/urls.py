from django.urls import path

import servers.views as vws

app_name = 'servers'

urlpatterns = [
    path('', vws.index, name='index'),
    path('server/', vws.add_server, name='server'),
]
