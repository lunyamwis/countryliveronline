from django.db import models
from core.models import TimeStamped, Supplier
from inventory.models import Item

class SeedLot(TimeStamped):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    crop_name = models.CharField(max_length=120)
    variety = models.CharField(max_length=120, blank=True)
    lot_code = models.CharField(max_length=80, blank=True)
    received_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    seed_count_est = models.PositiveIntegerField(default=0)
    storage_notes = models.TextField(blank=True)
    def __str__(self): return f"{self.crop_name} {self.variety}".strip()

class SeedTreatment(TimeStamped):
    seed_lot = models.ForeignKey(SeedLot, on_delete=models.CASCADE)
    treated_on = models.DateField()
    treatment_type = models.CharField(max_length=120)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    dosage = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.seed_lot} {self.treatment_type}"

class GerminationTest(TimeStamped):
    seed_lot = models.ForeignKey(SeedLot, on_delete=models.CASCADE)
    tested_on = models.DateField()
    sample_size = models.PositiveIntegerField(default=100)
    germinated = models.PositiveIntegerField(default=0)
    days_to_emerge = models.PositiveIntegerField(default=0)
    medium = models.CharField(max_length=80, blank=True)
    def __str__(self): return f"{self.seed_lot} test {self.tested_on}"
