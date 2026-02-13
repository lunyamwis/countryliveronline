from django.db import models
from core.models import TimeStamped, Location, Person, Supplier

class LandscapeProject(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=140)
    client_name = models.CharField(max_length=140, blank=True)
    status = models.CharField(max_length=40, default="active")
    budget_kes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class PlantCatalog(TimeStamped):
    common_name = models.CharField(max_length=120)
    botanical_name = models.CharField(max_length=140, blank=True)
    water_needs = models.CharField(max_length=60, blank=True)
    sun = models.CharField(max_length=60, blank=True)
    spacing_cm = models.PositiveIntegerField(default=30)
    notes = models.TextField(blank=True)
    def __str__(self): return self.common_name

class PlantingPlan(TimeStamped):
    project = models.ForeignKey(LandscapeProject, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantCatalog, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.project} - {self.plant}"

class IrrigationZone(TimeStamped):
    project = models.ForeignKey(LandscapeProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=80, blank=True)
    schedule = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.project} {self.name}"

class LandscapingWorkOrder(TimeStamped):
    project = models.ForeignKey(LandscapeProject, on_delete=models.CASCADE)
    date = models.DateField()
    task = models.CharField(max_length=160)
    assigned_to = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=40, default="todo")
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.task} {self.date}"
