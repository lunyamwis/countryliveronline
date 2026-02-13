from core.view_utils import make_crud
from .models import PoultryHouse, Flock, DailyRecord, FeedPlan, FeedingEvent, Vaccination, HealthIncident, EggProduction, SalesRecord
from .forms import PoultryHouseForm, FlockForm, DailyRecordForm, FeedPlanForm, FeedingEventForm, VaccinationForm, HealthIncidentForm, EggProductionForm, SalesRecordForm

_house = make_crud(
    model_=PoultryHouse, form_class_=PoultryHouseForm, prefix="poultry_house",
    search_fields=["name","ventilation","bedding_type","notes"],
    list_columns=[("name","House"),("location","Location"),("capacity_birds","Capacity"),("ventilation","Ventilation")],
)

_flock = make_crud(
    model_=Flock, form_class_=FlockForm, prefix="poultry_flock",
    search_fields=["batch_code","flock_type","source","status"],
    list_columns=[("batch_code","Batch"),("flock_type","Type"),("house","House"),("start_date","Start"),("current_count","Current")],
)

_daily = make_crud(
    model_=DailyRecord, form_class_=DailyRecordForm, prefix="poultry_daily",
    search_fields=["notes"],
    list_columns=[("flock","Flock"),("date","Date"),("mortality","Mortality"),("avg_weight_kg","Avg Wt"),("water_liters","Water(L)")],
)

_plan = make_crud(
    model_=FeedPlan, form_class_=FeedPlanForm, prefix="poultry_feedplan",
    search_fields=["phase"],
    list_columns=[("flock","Flock"),("phase","Phase"),("start_day","Start Day"),("end_day","End Day"),("target_fcr","Target FCR")],
)

_feed = make_crud(
    model_=FeedingEvent, form_class_=FeedingEventForm, prefix="poultry_feeding",
    search_fields=["method","notes"],
    list_columns=[("flock","Flock"),("date","Date"),("feed_item","Feed"),("qty_kg","Qty (kg)"),("method","Method")],
)

_vax = make_crud(
    model_=Vaccination, form_class_=VaccinationForm, prefix="poultry_vax",
    search_fields=["vaccine_name","route","notes"],
    list_columns=[("flock","Flock"),("date","Date"),("vaccine_name","Vaccine"),("route","Route"),("administered_by","By")],
)

_health = make_crud(
    model_=HealthIncident, form_class_=HealthIncidentForm, prefix="poultry_health",
    search_fields=["symptoms","suspected_diagnosis","action_taken"],
    list_columns=[("flock","Flock"),("date","Date"),("suspected_diagnosis","Dx"),("severity","Severity"),("resolved","Resolved")],
)

_eggs = make_crud(
    model_=EggProduction, form_class_=EggProductionForm, prefix="poultry_eggs",
    search_fields=["notes"],
    list_columns=[("flock","Flock"),("date","Date"),("eggs_count","Eggs"),("cracked","Cracked"),("trays","Trays")],
)

_sales = make_crud(
    model_=SalesRecord, form_class_=SalesRecordForm, prefix="poultry_sales",
    search_fields=["product","buyer"],
    list_columns=[("flock","Flock"),("date","Date"),("product","Product"),("qty","Qty"),("unit_price_kes","Unit Price")],
)

PoultryHouseList=_house["List"]; PoultryHouseDetail=_house["Detail"]; PoultryHouseCreate=_house["Create"]; PoultryHouseUpdate=_house["Update"]; PoultryHouseDelete=_house["Delete"]
FlockList=_flock["List"]; FlockDetail=_flock["Detail"]; FlockCreate=_flock["Create"]; FlockUpdate=_flock["Update"]; FlockDelete=_flock["Delete"]
DailyRecordList=_daily["List"]; DailyRecordDetail=_daily["Detail"]; DailyRecordCreate=_daily["Create"]; DailyRecordUpdate=_daily["Update"]; DailyRecordDelete=_daily["Delete"]
FeedPlanList=_plan["List"]; FeedPlanDetail=_plan["Detail"]; FeedPlanCreate=_plan["Create"]; FeedPlanUpdate=_plan["Update"]; FeedPlanDelete=_plan["Delete"]
FeedingEventList=_feed["List"]; FeedingEventDetail=_feed["Detail"]; FeedingEventCreate=_feed["Create"]; FeedingEventUpdate=_feed["Update"]; FeedingEventDelete=_feed["Delete"]
VaccinationList=_vax["List"]; VaccinationDetail=_vax["Detail"]; VaccinationCreate=_vax["Create"]; VaccinationUpdate=_vax["Update"]; VaccinationDelete=_vax["Delete"]
HealthIncidentList=_health["List"]; HealthIncidentDetail=_health["Detail"]; HealthIncidentCreate=_health["Create"]; HealthIncidentUpdate=_health["Update"]; HealthIncidentDelete=_health["Delete"]
EggProductionList=_eggs["List"]; EggProductionDetail=_eggs["Detail"]; EggProductionCreate=_eggs["Create"]; EggProductionUpdate=_eggs["Update"]; EggProductionDelete=_eggs["Delete"]
SalesRecordList=_sales["List"]; SalesRecordDetail=_sales["Detail"]; SalesRecordCreate=_sales["Create"]; SalesRecordUpdate=_sales["Update"]; SalesRecordDelete=_sales["Delete"]
