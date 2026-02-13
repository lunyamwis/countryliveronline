from django.contrib import admin
from .models import Item, StockBatch, StockUsage
admin.site.register(Item)
admin.site.register(StockBatch)
admin.site.register(StockUsage)
