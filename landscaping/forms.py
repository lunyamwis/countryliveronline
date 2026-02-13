from core.forms import BaseBSForm
from .models import LandscapeProject, PlantCatalog, PlantingPlan, IrrigationZone, LandscapingWorkOrder
class LandscapeProjectForm(BaseBSForm): 
    class Meta: model=LandscapeProject; fields="__all__"
class PlantCatalogForm(BaseBSForm): 
    class Meta: model=PlantCatalog; fields="__all__"
class PlantingPlanForm(BaseBSForm): 
    class Meta: model=PlantingPlan; fields="__all__"
class IrrigationZoneForm(BaseBSForm): 
    class Meta: model=IrrigationZone; fields="__all__"
class LandscapingWorkOrderForm(BaseBSForm): 
    class Meta: model=LandscapingWorkOrder; fields="__all__"
