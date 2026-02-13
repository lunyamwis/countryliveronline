from django.db import models
from core.models import TimeStamped, Asset, Person, Supplier
from inventory.models import Item

class FaultReport(TimeStamped):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    reported_on = models.DateField()
    fault = models.TextField()
    severity = models.CharField(max_length=40, default="medium")
    status = models.CharField(max_length=40, default="open")  # open/in_progress/resolved
    downtime_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self): return f"{self.asset} fault {self.reported_on}"

class RepairJob(TimeStamped):
    fault = models.ForeignKey(FaultReport, on_delete=models.CASCADE, related_name="jobs")
    started_on = models.DateField(null=True, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    technician = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True)
    external_vendor = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    labour_cost_kes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    def __str__(self): return f"RepairJob {self.fault_id}"

class RepairPartUsage(TimeStamped):
    repair_job = models.ForeignKey(RepairJob, on_delete=models.CASCADE, related_name="parts")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit_cost_kes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self): return f"{self.item} x{self.qty}"
