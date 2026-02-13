from django.db import models
from core.models import TimeStamped, Location
from organic.models import Crop

class GardenBed(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    length_m = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    width_m = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    sunlight = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class BedPlanting(TimeStamped):
    bed = models.ForeignKey(GardenBed, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)
    planted_on = models.DateField()
    method = models.CharField(max_length=80, blank=True)
    spacing = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=40, default="active")
    def __str__(self): return f"{self.bed} {self.planted_on}"

class BedHarvest(TimeStamped):
    planting = models.ForeignKey(BedPlanting, on_delete=models.CASCADE)
    harvested_on = models.DateField()
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, default="kg")
    def __str__(self): return f"{self.planting} {self.harvested_on}"
