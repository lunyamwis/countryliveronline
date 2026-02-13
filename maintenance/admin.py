from django.contrib import admin
from .models import MaintenancePlan, MaintenanceLog
admin.site.register(MaintenancePlan)
admin.site.register(MaintenanceLog)
