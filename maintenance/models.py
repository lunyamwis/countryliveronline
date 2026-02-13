from django.db import models
from core.models import TimeStamped, Asset, Person

class MaintenancePlan(TimeStamped):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    frequency_days = models.PositiveIntegerField(default=30)
    next_due = models.DateField()
    checklist = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.asset} every {self.frequency_days}d"

class MaintenanceLog(TimeStamped):
    plan = models.ForeignKey(MaintenancePlan, on_delete=models.CASCADE, related_name="logs")
    done_on = models.DateField()
    done_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    meter_reading = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    issues_found = models.TextField(blank=True)
    actions_taken = models.TextField(blank=True)
    status = models.CharField(max_length=40, default="done")
    def __str__(self): return f"{self.plan} {self.done_on}"
