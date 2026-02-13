from django.db import models
from core.models import TimeStamped, Supplier, Location

class Item(TimeStamped):
    CATEGORY = [
        ("seed","Seed"), ("fertilizer","Fertilizer"), ("pesticide","Pesticide"),
        ("feed","Animal Feed"), ("medicine","Medicine/Vet"), ("tool_part","Tool Part"),
        ("packaging","Packaging"), ("other","Other")
    ]
    name = models.CharField(max_length=160)
    category = models.CharField(max_length=40, choices=CATEGORY)
    unit = models.CharField(max_length=30, default="kg")
    reorder_level = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class StockBatch(TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    batch_code = models.CharField(max_length=80, blank=True)
    received_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    qty_received = models.DecimalField(max_digits=12, decimal_places=2)
    unit_cost_kes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    qty_remaining = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self): return f"{self.item} {self.batch_code}".strip()

class StockUsage(TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    used_on = models.DateField()
    qty_used = models.DecimalField(max_digits=12, decimal_places=2)
    purpose = models.CharField(max_length=200)
    def __str__(self): return f"{self.item} {self.used_on}"
