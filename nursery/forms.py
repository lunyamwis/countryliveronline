from core.forms import BaseBSForm
from .models import NurserySite, TrayBatch, NurseryDailyLog, SeedlingLoss, TransplantEvent
class NurserySiteForm(BaseBSForm): 
    class Meta: model=NurserySite; fields="__all__"
class TrayBatchForm(BaseBSForm): 
    class Meta: model=TrayBatch; fields="__all__"
class NurseryDailyLogForm(BaseBSForm): 
    class Meta: model=NurseryDailyLog; fields="__all__"
class SeedlingLossForm(BaseBSForm): 
    class Meta: model=SeedlingLoss; fields="__all__"
class TransplantEventForm(BaseBSForm): 
    class Meta: model=TransplantEvent; fields="__all__"
