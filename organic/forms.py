from core.forms import BaseBSForm
from .models import Plot, Crop, CropCycle, SoilTest, CompostBatch, FarmOperation, InputApplication, PestDiseaseIncident, Harvest

class PlotForm(BaseBSForm): 
    class Meta: model=Plot; fields="__all__"
class CropForm(BaseBSForm): 
    class Meta: model=Crop; fields="__all__"
class CropCycleForm(BaseBSForm): 
    class Meta: model=CropCycle; fields="__all__"
class SoilTestForm(BaseBSForm): 
    class Meta: model=SoilTest; fields="__all__"
class CompostBatchForm(BaseBSForm): 
    class Meta: model=CompostBatch; fields="__all__"
class FarmOperationForm(BaseBSForm): 
    class Meta: model=FarmOperation; fields="__all__"
class InputApplicationForm(BaseBSForm): 
    class Meta: model=InputApplication; fields="__all__"
class PestDiseaseIncidentForm(BaseBSForm): 
    class Meta: model=PestDiseaseIncident; fields="__all__"
class HarvestForm(BaseBSForm): 
    class Meta: model=Harvest; fields="__all__"
