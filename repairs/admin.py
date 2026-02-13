from django.contrib import admin
from .models import FaultReport, RepairJob, RepairPartUsage
admin.site.register(FaultReport)
admin.site.register(RepairJob)
admin.site.register(RepairPartUsage)
