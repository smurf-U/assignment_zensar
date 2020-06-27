from django.contrib import admin
from .models import RouterManager


@admin.register(RouterManager)
class RouterManagerAdmin(admin.ModelAdmin):
    list_display = ('sapid', 'hostname', 'loopback', 'mac_address')