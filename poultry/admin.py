from django.contrib import admin
from .models import PoultryHouse, Flock, DailyRecord, FeedPlan, FeedingEvent, Vaccination, HealthIncident, EggProduction, SalesRecord
admin.site.register(PoultryHouse)
admin.site.register(Flock)
admin.site.register(DailyRecord)
admin.site.register(FeedPlan)
admin.site.register(FeedingEvent)
admin.site.register(Vaccination)
admin.site.register(HealthIncident)
admin.site.register(EggProduction)
admin.site.register(SalesRecord)
