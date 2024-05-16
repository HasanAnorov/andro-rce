from django.contrib import admin
from .models import *

admin.site.register([Image, File, Message])

@admin.register(DeviceLocation)
class DeviceLocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'location', 'created', 'updated')
    search_fields = ('latitude', 'longitude', 'location')
    list_filter = ('created', 'updated')
    readonly_fields = ('id', 'created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('latitude', 'longitude', 'location', 'extra')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated')
        }),
    )