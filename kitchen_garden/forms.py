from core.forms import BaseBSForm
from .models import GardenBed, BedPlanting, BedHarvest
class GardenBedForm(BaseBSForm): 
    class Meta: model=GardenBed; fields="__all__"
class BedPlantingForm(BaseBSForm): 
    class Meta: model=BedPlanting; fields="__all__"
class BedHarvestForm(BaseBSForm): 
    class Meta: model=BedHarvest; fields="__all__"
