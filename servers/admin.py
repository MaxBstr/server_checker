from django.contrib import admin

from servers.models import UserProfile, Server

admin.site.register(UserProfile)
admin.site.register(Server)
