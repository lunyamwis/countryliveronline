from core.forms import BaseBSForm
from .models import MaintenancePlan, MaintenanceLog
class MaintenancePlanForm(BaseBSForm): 
    class Meta: model=MaintenancePlan; fields="__all__"
class MaintenanceLogForm(BaseBSForm): 
    class Meta: model=MaintenanceLog; fields="__all__"
