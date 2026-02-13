from core.view_utils import make_crud
from .models import Plot, Crop, CropCycle, SoilTest, CompostBatch, FarmOperation, InputApplication, PestDiseaseIncident, Harvest
from .forms import PlotForm, CropForm, CropCycleForm, SoilTestForm, CompostBatchForm, FarmOperationForm, InputApplicationForm, PestDiseaseIncidentForm, HarvestForm

_plot = make_crud(
    model_=Plot, form_class_=PlotForm, prefix="organic_plot",
    search_fields=["name","soil_type","irrigation","notes"],
    list_columns=[("name","Plot"),("location","Location"),("area_acres","Acres"),("soil_type","Soil"),("irrigation","Irrigation")],
)

_crop = make_crud(
    model_=Crop, form_class_=CropForm, prefix="organic_crop",
    search_fields=["name","variety","notes"],
    list_columns=[("name","Crop"),("variety","Variety"),("maturity_days","Maturity (days)"),("spacing_cm","Spacing")],
)

_cycle = make_crud(
    model_=CropCycle, form_class_=CropCycleForm, prefix="organic_cycle",
    search_fields=["status"],
    list_columns=[("plot","Plot"),("crop","Crop"),("start_date","Start"),("expected_end_date","Expected End"),("status","Status")],
)

_soil = make_crud(
    model_=SoilTest, form_class_=SoilTestForm, prefix="organic_soiltest",
    search_fields=["notes"],
    list_columns=[("plot","Plot"),("tested_on","Tested On"),("ph","pH"),("organic_matter_pct","OM %")],
)

_compost = make_crud(
    model_=CompostBatch, form_class_=CompostBatchForm, prefix="organic_compost",
    search_fields=["method","inputs","status"],
    list_columns=[("location","Location"),("started_on","Started"),("method","Method"),("turned_count","Turns"),("status","Status")],
)

_op = make_crud(
    model_=FarmOperation, form_class_=FarmOperationForm, prefix="organic_operation",
    search_fields=["operation_type","notes"],
    list_columns=[("cycle","Cycle"),("done_on","Date"),("operation_type","Operation"),("labourer","Labourer")],
)

_input = make_crud(
    model_=InputApplication, form_class_=InputApplicationForm, prefix="organic_input",
    search_fields=["method","reason"],
    list_columns=[("cycle","Cycle"),("item","Item"),("applied_on","Date"),("qty","Qty"),("method","Method")],
)

_pest = make_crud(
    model_=PestDiseaseIncident, form_class_=PestDiseaseIncidentForm, prefix="organic_pest",
    search_fields=["type","severity","action_taken"],
    list_columns=[("cycle","Cycle"),("observed_on","Observed"),("type","Type"),("severity","Severity"),("resolved","Resolved")],
)

_harv = make_crud(
    model_=Harvest, form_class_=HarvestForm, prefix="organic_harvest",
    search_fields=["grade"],
    list_columns=[("cycle","Cycle"),("harvested_on","Harvested"),("qty_kg","Qty (kg)"),("losses_kg","Losses"),("grade","Grade")],
)

PlotList=_plot["List"]; PlotDetail=_plot["Detail"]; PlotCreate=_plot["Create"]; PlotUpdate=_plot["Update"]; PlotDelete=_plot["Delete"]
CropList=_crop["List"]; CropDetail=_crop["Detail"]; CropCreate=_crop["Create"]; CropUpdate=_crop["Update"]; CropDelete=_crop["Delete"]
CycleList=_cycle["List"]; CycleDetail=_cycle["Detail"]; CycleCreate=_cycle["Create"]; CycleUpdate=_cycle["Update"]; CycleDelete=_cycle["Delete"]
SoilTestList=_soil["List"]; SoilTestDetail=_soil["Detail"]; SoilTestCreate=_soil["Create"]; SoilTestUpdate=_soil["Update"]; SoilTestDelete=_soil["Delete"]
CompostList=_compost["List"]; CompostDetail=_compost["Detail"]; CompostCreate=_compost["Create"]; CompostUpdate=_compost["Update"]; CompostDelete=_compost["Delete"]
OperationList=_op["List"]; OperationDetail=_op["Detail"]; OperationCreate=_op["Create"]; OperationUpdate=_op["Update"]; OperationDelete=_op["Delete"]
InputList=_input["List"]; InputDetail=_input["Detail"]; InputCreate=_input["Create"]; InputUpdate=_input["Update"]; InputDelete=_input["Delete"]
PestList=_pest["List"]; PestDetail=_pest["Detail"]; PestCreate=_pest["Create"]; PestUpdate=_pest["Update"]; PestDelete=_pest["Delete"]
HarvestList=_harv["List"]; HarvestDetail=_harv["Detail"]; HarvestCreate=_harv["Create"]; HarvestUpdate=_harv["Update"]; HarvestDelete=_harv["Delete"]
