from django.db import models
from core.models import TimeStamped, Location, Person
from inventory.models import Item

class PoultryHouse(TimeStamped):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    capacity_birds = models.PositiveIntegerField(default=0)
    ventilation = models.CharField(max_length=120, blank=True)
    bedding_type = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class Flock(TimeStamped):
    FLOCK_TYPE = [("broiler","Broiler"),("layer","Layer"),("kienyeji","Kienyeji")]
    house = models.ForeignKey(PoultryHouse, on_delete=models.SET_NULL, null=True, blank=True)
    flock_type = models.CharField(max_length=40, choices=FLOCK_TYPE)
    batch_code = models.CharField(max_length=80)
    source = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    initial_count = models.PositiveIntegerField()
    current_count = models.PositiveIntegerField()
    status = models.CharField(max_length=40, default="active")
    def __str__(self): return f"{self.batch_code} ({self.flock_type})"

class DailyRecord(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    mortality = models.PositiveIntegerField(default=0)
    culled = models.PositiveIntegerField(default=0)
    avg_weight_kg = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    water_liters = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.flock} {self.date}"

class FeedPlan(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    phase = models.CharField(max_length=60)
    start_day = models.PositiveIntegerField(default=1)
    end_day = models.PositiveIntegerField(default=14)
    target_fcr = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self): return f"{self.flock} {self.phase}"

class FeedingEvent(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    feed_item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    qty_kg = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.flock} feed {self.date}"

class Vaccination(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    vaccine_name = models.CharField(max_length=120)
    route = models.CharField(max_length=80, blank=True)
    administered_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.vaccine_name} {self.date}"

class HealthIncident(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    symptoms = models.TextField()
    suspected_diagnosis = models.CharField(max_length=120, blank=True)
    severity = models.CharField(max_length=40, default="medium")
    action_taken = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)
    def __str__(self): return f"Health {self.flock} {self.date}"

class EggProduction(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    eggs_count = models.PositiveIntegerField(default=0)
    cracked = models.PositiveIntegerField(default=0)
    trays = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return f"Eggs {self.flock} {self.date}"

class SalesRecord(TimeStamped):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    product = models.CharField(max_length=80)
    qty = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price_kes = models.DecimalField(max_digits=12, decimal_places=2)
    buyer = models.CharField(max_length=140, blank=True)
    def __str__(self): return f"Sale {self.product} {self.date}"
