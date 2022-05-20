from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('servers.urls', namespace='servers')),
    path('admin/', admin.site.urls),
]
