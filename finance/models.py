from django.db import models
from core.models import TimeStamped, Supplier, Location

class Expense(TimeStamped):
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    amount_kes = models.DecimalField(max_digits=12, decimal_places=2)
    ref = models.CharField(max_length=80, blank=True)
    def __str__(self): return f"Expense {self.date} {self.amount_kes}"

class Income(TimeStamped):
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    source = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True)
    amount_kes = models.DecimalField(max_digits=12, decimal_places=2)
    buyer = models.CharField(max_length=140, blank=True)
    def __str__(self): return f"Income {self.date} {self.amount_kes}"
