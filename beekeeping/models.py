from django.db import models
from core.models import TimeStamped, Location, Person, Asset

class Apiary(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    forage_notes = models.TextField(blank=True)
    water_source = models.CharField(max_length=120, blank=True)
    def __str__(self): return self.name

class Hive(TimeStamped):
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)
    asset = models.OneToOneField(Asset, on_delete=models.SET_NULL, null=True, blank=True)
    hive_type = models.CharField(max_length=60, default="langstroth")
    hive_code = models.CharField(max_length=80)
    installed_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=40, default="active")
    def __str__(self): return self.hive_code

class HiveInspection(TimeStamped):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    date = models.DateField()
    inspector = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    queen_seen = models.BooleanField(default=False)
    brood_present = models.BooleanField(default=False)
    honey_frames = models.PositiveIntegerField(default=0)
    pests = models.CharField(max_length=160, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"Inspect {self.hive} {self.date}"

class Feeding(TimeStamped):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    date = models.DateField()
    feed_type = models.CharField(max_length=80)
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return f"Feed {self.hive} {self.date}"

class HarvestBatch(TimeStamped):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    harvested_on = models.DateField()
    honey_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wax_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moisture_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=60, blank=True)
    def __str__(self): return f"Harvest {self.hive} {self.harvested_on}"
