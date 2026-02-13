from django.contrib import admin
from .models import NurserySite, TrayBatch, NurseryDailyLog, SeedlingLoss, TransplantEvent
admin.site.register(NurserySite)
admin.site.register(TrayBatch)
admin.site.register(NurseryDailyLog)
admin.site.register(SeedlingLoss)
admin.site.register(TransplantEvent)
