from django.contrib import admin
from .models import SeedLot, SeedTreatment, GerminationTest
admin.site.register(SeedLot)
admin.site.register(SeedTreatment)
admin.site.register(GerminationTest)
