from core.forms import BaseBSForm
from .models import FaultReport, RepairJob, RepairPartUsage
class FaultReportForm(BaseBSForm): 
    class Meta: model=FaultReport; fields="__all__"
class RepairJobForm(BaseBSForm): 
    class Meta: model=RepairJob; fields="__all__"
class RepairPartUsageForm(BaseBSForm): 
    class Meta: model=RepairPartUsage; fields="__all__"
