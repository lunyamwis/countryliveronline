from core.view_utils import make_crud
from .models import GardenBed, BedPlanting, BedHarvest
from .forms import GardenBedForm, BedPlantingForm, BedHarvestForm

_bed = make_crud(
    model_=GardenBed, form_class_=GardenBedForm, prefix="kitchen_bed",
    search_fields=["name","sunlight","notes"],
    list_columns=[("name","Bed"),("location","Location"),("length_m","Length"),("width_m","Width"),("sunlight","Sunlight")],
)

_plant = make_crud(
    model_=BedPlanting, form_class_=BedPlantingForm, prefix="kitchen_planting",
    search_fields=["method","spacing","status"],
    list_columns=[("bed","Bed"),("crop","Crop"),("planted_on","Planted"),("method","Method"),("status","Status")],
)

_h = make_crud(
    model_=BedHarvest, form_class_=BedHarvestForm, prefix="kitchen_harvest",
    search_fields=["unit"],
    list_columns=[("planting","Planting"),("harvested_on","Harvested"),("qty","Qty"),("unit","Unit")],
)

GardenBedList=_bed["List"]; GardenBedDetail=_bed["Detail"]; GardenBedCreate=_bed["Create"]; GardenBedUpdate=_bed["Update"]; GardenBedDelete=_bed["Delete"]
BedPlantingList=_plant["List"]; BedPlantingDetail=_plant["Detail"]; BedPlantingCreate=_plant["Create"]; BedPlantingUpdate=_plant["Update"]; BedPlantingDelete=_plant["Delete"]
BedHarvestList=_h["List"]; BedHarvestDetail=_h["Detail"]; BedHarvestCreate=_h["Create"]; BedHarvestUpdate=_h["Update"]; BedHarvestDelete=_h["Delete"]
