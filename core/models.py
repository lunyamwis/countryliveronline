from django.db import models
from django.utils import timezone

class TimeStamped(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Location(TimeStamped):
    name = models.CharField(max_length=120)
    county = models.CharField(max_length=80, blank=True)
    ward = models.CharField(max_length=80, blank=True)
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class Supplier(TimeStamped):
    name = models.CharField(max_length=140)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=140, blank=True)
    categories = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class Person(TimeStamped):
    full_name = models.CharField(max_length=140)
    phone = models.CharField(max_length=40, blank=True)
    role = models.CharField(max_length=80, blank=True)
    def __str__(self): return self.full_name

class Asset(TimeStamped):
    ASSET_TYPES = [
        ("tool","Tool"), ("machine","Machine"), ("vehicle","Vehicle"),
        ("building","Building"), ("irrigation","Irrigation"), ("hive","Hive"), ("poultry_house","Poultry House")
    ]
    name = models.CharField(max_length=140)
    asset_type = models.CharField(max_length=30, choices=ASSET_TYPES)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    serial_number = models.CharField(max_length=80, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_cost_kes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default="active")
    notes = models.TextField(blank=True)
    def __str__(self): return self.name

class Task(TimeStamped):
    PRIORITY = [("low","Low"),("medium","Medium"),("high","High"),("urgent","Urgent")]
    STATUS = [("todo","To Do"),("doing","Doing"),("done","Done"),("blocked","Blocked")]
    title = models.CharField(max_length=160)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY, default="medium")
    status = models.CharField(max_length=20, choices=STATUS, default="todo")
    notes = models.TextField(blank=True)
    def __str__(self): return self.title
