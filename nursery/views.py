from core.view_utils import make_crud
from .models import NurserySite, TrayBatch, NurseryDailyLog, SeedlingLoss, TransplantEvent
from .forms import NurserySiteForm, TrayBatchForm, NurseryDailyLogForm, SeedlingLossForm, TransplantEventForm

_site = make_crud(
    model_=NurserySite, form_class_=NurserySiteForm, prefix="nursery_site",
    search_fields=["name","water_source","notes"],
    list_columns=[("name","Site"),("location","Location"),("shade_net","Shade Net"),("water_source","Water")],
)

_batch = make_crud(
    model_=TrayBatch, form_class_=TrayBatchForm, prefix="nursery_batch",
    search_fields=["crop_name","variety","status","medium"],
    list_columns=[("site","Site"),("crop_name","Crop"),("variety","Variety"),("started_on","Started"),("status","Status")],
)

_log = make_crud(
    model_=NurseryDailyLog, form_class_=NurseryDailyLogForm, prefix="nursery_log",
    search_fields=["notes"],
    list_columns=[("batch","Batch"),("date","Date"),("watered","Watered"),("fertilizer_applied","Fertilizer"),("pest_observed","Pest")],
)

_loss = make_crud(
    model_=SeedlingLoss, form_class_=SeedlingLossForm, prefix="nursery_loss",
    search_fields=["reason","action_taken"],
    list_columns=[("batch","Batch"),("date","Date"),("lost_count","Lost"),("reason","Reason")],
)

_trans = make_crud(
    model_=TransplantEvent, form_class_=TransplantEventForm, prefix="nursery_transplant",
    search_fields=["destination"],
    list_columns=[("batch","Batch"),("date","Date"),("transplanted_count","Count"),("destination","Destination"),("supervised_by","Supervisor")],
)

NurserySiteList=_site["List"]; NurserySiteDetail=_site["Detail"]; NurserySiteCreate=_site["Create"]; NurserySiteUpdate=_site["Update"]; NurserySiteDelete=_site["Delete"]
TrayBatchList=_batch["List"]; TrayBatchDetail=_batch["Detail"]; TrayBatchCreate=_batch["Create"]; TrayBatchUpdate=_batch["Update"]; TrayBatchDelete=_batch["Delete"]
NurseryDailyLogList=_log["List"]; NurseryDailyLogDetail=_log["Detail"]; NurseryDailyLogCreate=_log["Create"]; NurseryDailyLogUpdate=_log["Update"]; NurseryDailyLogDelete=_log["Delete"]
SeedlingLossList=_loss["List"]; SeedlingLossDetail=_loss["Detail"]; SeedlingLossCreate=_loss["Create"]; SeedlingLossUpdate=_loss["Update"]; SeedlingLossDelete=_loss["Delete"]
TransplantEventList=_trans["List"]; TransplantEventDetail=_trans["Detail"]; TransplantEventCreate=_trans["Create"]; TransplantEventUpdate=_trans["Update"]; TransplantEventDelete=_trans["Delete"]
