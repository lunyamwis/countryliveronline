from core.view_utils import make_crud
from .models import MaintenancePlan, MaintenanceLog
from .forms import MaintenancePlanForm, MaintenanceLogForm

_plan = make_crud(
    model_=MaintenancePlan, form_class_=MaintenancePlanForm, prefix="maint_plan",
    search_fields=["checklist","notes"],
    list_columns=[("asset","Asset"),("frequency_days","Freq (days)"),("next_due","Next Due")],
)

_log = make_crud(
    model_=MaintenanceLog, form_class_=MaintenanceLogForm, prefix="maint_log",
    search_fields=["issues_found","actions_taken"],
    list_columns=[("plan","Plan"),("done_on","Done On"),("done_by","By"),("meter_reading","Meter"),("status","Status")],
)

MaintenancePlanList=_plan["List"]; MaintenancePlanDetail=_plan["Detail"]; MaintenancePlanCreate=_plan["Create"]; MaintenancePlanUpdate=_plan["Update"]; MaintenancePlanDelete=_plan["Delete"]
MaintenanceLogList=_log["List"]; MaintenanceLogDetail=_log["Detail"]; MaintenanceLogCreate=_log["Create"]; MaintenanceLogUpdate=_log["Update"]; MaintenanceLogDelete=_log["Delete"]
