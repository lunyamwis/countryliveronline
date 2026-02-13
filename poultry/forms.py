from core.forms import BaseBSForm
from .models import PoultryHouse, Flock, DailyRecord, FeedPlan, FeedingEvent, Vaccination, HealthIncident, EggProduction, SalesRecord
class PoultryHouseForm(BaseBSForm): 
    class Meta: model=PoultryHouse; fields="__all__"
class FlockForm(BaseBSForm): 
    class Meta: model=Flock; fields="__all__"
class DailyRecordForm(BaseBSForm): 
    class Meta: model=DailyRecord; fields="__all__"
class FeedPlanForm(BaseBSForm): 
    class Meta: model=FeedPlan; fields="__all__"
class FeedingEventForm(BaseBSForm): 
    class Meta: model=FeedingEvent; fields="__all__"
class VaccinationForm(BaseBSForm): 
    class Meta: model=Vaccination; fields="__all__"
class HealthIncidentForm(BaseBSForm): 
    class Meta: model=HealthIncident; fields="__all__"
class EggProductionForm(BaseBSForm): 
    class Meta: model=EggProduction; fields="__all__"
class SalesRecordForm(BaseBSForm): 
    class Meta: model=SalesRecord; fields="__all__"
