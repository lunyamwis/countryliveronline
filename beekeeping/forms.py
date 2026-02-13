from core.forms import BaseBSForm
from .models import Apiary, Hive, HiveInspection, Feeding, HarvestBatch
class ApiaryForm(BaseBSForm): 
    class Meta: model=Apiary; fields="__all__"
class HiveForm(BaseBSForm): 
    class Meta: model=Hive; fields="__all__"
class HiveInspectionForm(BaseBSForm): 
    class Meta: model=HiveInspection; fields="__all__"
class FeedingForm(BaseBSForm): 
    class Meta: model=Feeding; fields="__all__"
class HarvestBatchForm(BaseBSForm): 
    class Meta: model=HarvestBatch; fields="__all__"
