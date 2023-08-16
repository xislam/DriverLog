from django.contrib import admin
from .models import DriverLog


class DriverLogAdmin(admin.ModelAdmin):
    list_display = ('driver_id', 'create_date', 'status')
    actions = ['calculate_working_time']


admin.site.register(DriverLog, DriverLogAdmin)
