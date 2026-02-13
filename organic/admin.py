from django.contrib import admin
from .models import Plot, Crop, CropCycle, SoilTest, CompostBatch, FarmOperation, InputApplication, PestDiseaseIncident, Harvest
admin.site.register(Plot)
admin.site.register(Crop)
admin.site.register(CropCycle)
admin.site.register(SoilTest)
admin.site.register(CompostBatch)
admin.site.register(FarmOperation)
admin.site.register(InputApplication)
admin.site.register(PestDiseaseIncident)
admin.site.register(Harvest)
