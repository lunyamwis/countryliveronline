from django.db import models
from core.models import TimeStamped, Location, Person
from inventory.models import Item

class Plot(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    area_acres = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    soil_type = models.CharField(max_length=80, blank=True)
    irrigation = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class Crop(TimeStamped):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=120, blank=True)
    maturity_days = models.PositiveIntegerField(default=60)
    spacing_cm = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.name} {self.variety}".strip()

class CropCycle(TimeStamped):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    start_date = models.DateField()
    expected_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=40, default="active")
    target_yield_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self): return f"{self.plot} - {self.crop} ({self.start_date})"

class SoilTest(TimeStamped):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    tested_on = models.DateField()
    ph = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ec = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    nitrogen = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    phosphorus = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    potassium = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    organic_matter_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"SoilTest {self.plot} {self.tested_on}"

class CompostBatch(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    started_on = models.DateField()
    method = models.CharField(max_length=80, default="3-bay")
    inputs = models.TextField(blank=True)
    moisture_check = models.CharField(max_length=80, blank=True)
    turned_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=40, default="active")
    estimated_qty_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self): return f"Compost {self.started_on} ({self.status})"

class FarmOperation(TimeStamped):
    cycle = models.ForeignKey(CropCycle, on_delete=models.CASCADE, related_name="operations")
    done_on = models.DateField()
    operation_type = models.CharField(max_length=80)
    labourer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.operation_type} {self.done_on}"

class InputApplication(TimeStamped):
    cycle = models.ForeignKey(CropCycle, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    applied_on = models.DateField()
    qty = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=80, blank=True)
    reason = models.CharField(max_length=200, blank=True)
    def __str__(self): return f"{self.item} {self.applied_on}"

class PestDiseaseIncident(TimeStamped):
    cycle = models.ForeignKey(CropCycle, on_delete=models.CASCADE)
    observed_on = models.DateField()
    type = models.CharField(max_length=120)
    severity = models.CharField(max_length=40, default="medium")
    action_taken = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)
    def __str__(self): return f"{self.type} {self.observed_on}"

class Harvest(TimeStamped):
    cycle = models.ForeignKey(CropCycle, on_delete=models.CASCADE)
    harvested_on = models.DateField()
    qty_kg = models.DecimalField(max_digits=12, decimal_places=2)
    grade = models.CharField(max_length=60, blank=True)
    losses_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self): return f"Harvest {self.harvested_on} {self.qty_kg}kg"
