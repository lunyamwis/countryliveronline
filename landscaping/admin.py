from django.contrib import admin
from .models import LandscapeProject, PlantCatalog, PlantingPlan, IrrigationZone, LandscapingWorkOrder
admin.site.register(LandscapeProject)
admin.site.register(PlantCatalog)
admin.site.register(PlantingPlan)
admin.site.register(IrrigationZone)
admin.site.register(LandscapingWorkOrder)
