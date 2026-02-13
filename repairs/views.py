from core.view_utils import make_crud
from .models import FaultReport, RepairJob, RepairPartUsage
from .forms import FaultReportForm, RepairJobForm, RepairPartUsageForm

_fault = make_crud(
    model_=FaultReport, form_class_=FaultReportForm, prefix="rep_fault",
    search_fields=["fault","severity","status"],
    list_columns=[("asset","Asset"),("reported_on","Reported On"),("severity","Severity"),("status","Status"),("downtime_hours","Downtime (h)")],
)

_job = make_crud(
    model_=RepairJob, form_class_=RepairJobForm, prefix="rep_job",
    search_fields=["notes"],
    list_columns=[("fault","Fault"),("started_on","Started"),("completed_on","Completed"),("technician","Technician"),("labour_cost_kes","Labour (KES)")],
)

_part = make_crud(
    model_=RepairPartUsage, form_class_=RepairPartUsageForm, prefix="rep_part",
    search_fields=[],
    list_columns=[("repair_job","Job"),("item","Part"),("qty","Qty"),("unit_cost_kes","Unit Cost")],
)

FaultReportList=_fault["List"]; FaultReportDetail=_fault["Detail"]; FaultReportCreate=_fault["Create"]; FaultReportUpdate=_fault["Update"]; FaultReportDelete=_fault["Delete"]
RepairJobList=_job["List"]; RepairJobDetail=_job["Detail"]; RepairJobCreate=_job["Create"]; RepairJobUpdate=_job["Update"]; RepairJobDelete=_job["Delete"]
RepairPartUsageList=_part["List"]; RepairPartUsageDetail=_part["Detail"]; RepairPartUsageCreate=_part["Create"]; RepairPartUsageUpdate=_part["Update"]; RepairPartUsageDelete=_part["Delete"]
