from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('servers.urls', namespace='servers')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
