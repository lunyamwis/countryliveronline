from django.contrib import admin
from .models import Apiary, Hive, HiveInspection, Feeding, HarvestBatch
admin.site.register(Apiary)
admin.site.register(Hive)
admin.site.register(HiveInspection)
admin.site.register(Feeding)
admin.site.register(HarvestBatch)
