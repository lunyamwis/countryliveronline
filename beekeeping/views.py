from core.view_utils import make_crud
from .models import Apiary, Hive, HiveInspection, Feeding, HarvestBatch
from .forms import ApiaryForm, HiveForm, HiveInspectionForm, FeedingForm, HarvestBatchForm

_api = make_crud(
    model_=Apiary, form_class_=ApiaryForm, prefix="bee_apiary",
    search_fields=["name","forage_notes","water_source"],
    list_columns=[("name","Apiary"),("location","Location"),("water_source","Water")],
)

_hive = make_crud(
    model_=Hive, form_class_=HiveForm, prefix="bee_hive",
    search_fields=["hive_code","hive_type","status"],
    list_columns=[("hive_code","Code"),("apiary","Apiary"),("hive_type","Type"),("installed_on","Installed"),("status","Status")],
)

_ins = make_crud(
    model_=HiveInspection, form_class_=HiveInspectionForm, prefix="bee_inspection",
    search_fields=["pests","notes"],
    list_columns=[("hive","Hive"),("date","Date"),("inspector","Inspector"),("queen_seen","Queen"),("honey_frames","Honey Frames")],
)

_feed = make_crud(
    model_=Feeding, form_class_=FeedingForm, prefix="bee_feeding",
    search_fields=["feed_type","notes"],
    list_columns=[("hive","Hive"),("date","Date"),("feed_type","Feed Type"),("qty","Qty")],
)

_harv = make_crud(
    model_=HarvestBatch, form_class_=HarvestBatchForm, prefix="bee_harvest",
    search_fields=["grade"],
    list_columns=[("hive","Hive"),("harvested_on","Harvested"),("honey_kg","Honey (kg)"),("wax_kg","Wax (kg)"),("moisture_pct","Moisture %")],
)

ApiaryList=_api["List"]; ApiaryDetail=_api["Detail"]; ApiaryCreate=_api["Create"]; ApiaryUpdate=_api["Update"]; ApiaryDelete=_api["Delete"]
HiveList=_hive["List"]; HiveDetail=_hive["Detail"]; HiveCreate=_hive["Create"]; HiveUpdate=_hive["Update"]; HiveDelete=_hive["Delete"]
HiveInspectionList=_ins["List"]; HiveInspectionDetail=_ins["Detail"]; HiveInspectionCreate=_ins["Create"]; HiveInspectionUpdate=_ins["Update"]; HiveInspectionDelete=_ins["Delete"]
FeedingList=_feed["List"]; FeedingDetail=_feed["Detail"]; FeedingCreate=_feed["Create"]; FeedingUpdate=_feed["Update"]; FeedingDelete=_feed["Delete"]
HarvestBatchList=_harv["List"]; HarvestBatchDetail=_harv["Detail"]; HarvestBatchCreate=_harv["Create"]; HarvestBatchUpdate=_harv["Update"]; HarvestBatchDelete=_harv["Delete"]
