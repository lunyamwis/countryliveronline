from core.view_utils import make_crud
from .models import LandscapeProject, PlantCatalog, PlantingPlan, IrrigationZone, LandscapingWorkOrder
from .forms import LandscapeProjectForm, PlantCatalogForm, PlantingPlanForm, IrrigationZoneForm, LandscapingWorkOrderForm

_proj = make_crud(
    model_=LandscapeProject, form_class_=LandscapeProjectForm, prefix="land_project",
    search_fields=["name","client_name","status","notes"],
    list_columns=[("name","Project"),("location","Location"),("status","Status"),("budget_kes","Budget"),("client_name","Client")],
)

_cat = make_crud(
    model_=PlantCatalog, form_class_=PlantCatalogForm, prefix="land_plant",
    search_fields=["common_name","botanical_name","notes"],
    list_columns=[("common_name","Common"),("botanical_name","Botanical"),("water_needs","Water"),("sun","Sun"),("spacing_cm","Spacing")],
)

_plan = make_crud(
    model_=PlantingPlan, form_class_=PlantingPlanForm, prefix="land_plan",
    search_fields=["area","notes"],
    list_columns=[("project","Project"),("plant","Plant"),("qty","Qty"),("supplier","Supplier"),("area","Area")],
)

_zone = make_crud(
    model_=IrrigationZone, form_class_=IrrigationZoneForm, prefix="land_zone",
    search_fields=["name","type","schedule","notes"],
    list_columns=[("project","Project"),("name","Zone"),("type","Type"),("schedule","Schedule")],
)

_work = make_crud(
    model_=LandscapingWorkOrder, form_class_=LandscapingWorkOrderForm, prefix="land_work",
    search_fields=["task","status","notes"],
    list_columns=[("project","Project"),("date","Date"),("task","Task"),("assigned_to","Assigned"),("status","Status")],
)

LandscapeProjectList=_proj["List"]; LandscapeProjectDetail=_proj["Detail"]; LandscapeProjectCreate=_proj["Create"]; LandscapeProjectUpdate=_proj["Update"]; LandscapeProjectDelete=_proj["Delete"]
PlantCatalogList=_cat["List"]; PlantCatalogDetail=_cat["Detail"]; PlantCatalogCreate=_cat["Create"]; PlantCatalogUpdate=_cat["Update"]; PlantCatalogDelete=_cat["Delete"]
PlantingPlanList=_plan["List"]; PlantingPlanDetail=_plan["Detail"]; PlantingPlanCreate=_plan["Create"]; PlantingPlanUpdate=_plan["Update"]; PlantingPlanDelete=_plan["Delete"]
IrrigationZoneList=_zone["List"]; IrrigationZoneDetail=_zone["Detail"]; IrrigationZoneCreate=_zone["Create"]; IrrigationZoneUpdate=_zone["Update"]; IrrigationZoneDelete=_zone["Delete"]
LandscapingWorkOrderList=_work["List"]; LandscapingWorkOrderDetail=_work["Detail"]; LandscapingWorkOrderCreate=_work["Create"]; LandscapingWorkOrderUpdate=_work["Update"]; LandscapingWorkOrderDelete=_work["Delete"]
