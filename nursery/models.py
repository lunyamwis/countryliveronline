from django.db import models
from core.models import TimeStamped, Location, Person
from propagation.models import SeedLot

class NurserySite(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    shade_net = models.BooleanField(default=True)
    water_source = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class TrayBatch(TimeStamped):
    site = models.ForeignKey(NurserySite, on_delete=models.CASCADE)
    seed_lot = models.ForeignKey(SeedLot, on_delete=models.SET_NULL, null=True, blank=True)
    crop_name = models.CharField(max_length=120)
    variety = models.CharField(max_length=120, blank=True)
    started_on = models.DateField()
    trays_count = models.PositiveIntegerField(default=0)
    cells_per_tray = models.PositiveIntegerField(default=128)
    medium = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=40, default="active")
    def __str__(self): return f"{self.crop_name} {self.started_on}"

class NurseryDailyLog(TimeStamped):
    batch = models.ForeignKey(TrayBatch, on_delete=models.CASCADE)
    date = models.DateField()
    watered = models.BooleanField(default=False)
    fertilizer_applied = models.BooleanField(default=False)
    pest_observed = models.BooleanField(default=False)
    disease_observed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    def __str__(self): return f"Log {self.batch} {self.date}"

class SeedlingLoss(TimeStamped):
    batch = models.ForeignKey(TrayBatch, on_delete=models.CASCADE)
    date = models.DateField()
    lost_count = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=160)
    action_taken = models.TextField(blank=True)
    def __str__(self): return f"Loss {self.batch} {self.date}"

class TransplantEvent(TimeStamped):
    batch = models.ForeignKey(TrayBatch, on_delete=models.CASCADE)
    date = models.DateField()
    transplanted_count = models.PositiveIntegerField(default=0)
    destination = models.CharField(max_length=160, blank=True)
    supervised_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return f"Transplant {self.batch} {self.date}"
