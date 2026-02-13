from django.views.generic import TemplateView
from django.db.models import Count

from .models import Location, Supplier, Person, Asset, Task
from .forms import LocationForm, SupplierForm, PersonForm, AssetForm, TaskForm
from .view_utils import make_crud

# Dashboard
class DashboardView(TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # lightweight KPIs (counts)
        from organic.models import CropCycle
        from poultry.models import Flock
        from beekeeping.models import Hive
        from repairs.models import FaultReport
        from maintenance.models import MaintenancePlan
        from inventory.models import Item

        ctx["kpis"] = {
            "locations": Location.objects.count(),
            "assets": Asset.objects.count(),
            "tasks_open": Task.objects.exclude(status="done").count(),
            "active_cycles": CropCycle.objects.filter(status="active").count(),
            "active_flocks": Flock.objects.filter(status="active").count(),
            "active_hives": Hive.objects.filter(status="active").count(),
            "open_faults": FaultReport.objects.filter(status__in=["open","in_progress"]).count(),
            "maintenance_plans": MaintenancePlan.objects.count(),
            "inventory_items": Item.objects.count(),
        }
        return ctx

# CRUDs
_location = make_crud(
    model_=Location, form_class_=LocationForm, prefix="core_location",
    search_fields=["name", "county", "ward", "notes"],
    list_columns=[("name","Name"),("county","County"),("ward","Ward"),("gps_lat","Lat"),("gps_lon","Lon")],
    detail_groups=[
        {"title":"Location", "fields":[("name","Name"),("county","County"),("ward","Ward")]},
        {"title":"Coordinates & Notes", "fields":[("gps_lat","Latitude"),("gps_lon","Longitude"),("notes","Notes")]}
    ],
)

_supplier = make_crud(
    model_=Supplier, form_class_=SupplierForm, prefix="core_supplier",
    search_fields=["name","phone","email","location","categories","notes"],
    list_columns=[("name","Name"),("phone","Phone"),("categories","Categories"),("location","Location")],
)

_person = make_crud(
    model_=Person, form_class_=PersonForm, prefix="core_person",
    search_fields=["full_name","phone","role"],
    list_columns=[("full_name","Full Name"),("role","Role"),("phone","Phone")],
)

_asset = make_crud(
    model_=Asset, form_class_=AssetForm, prefix="core_asset",
    search_fields=["name","asset_type","serial_number","status","notes"],
    list_columns=[("name","Name"),("asset_type","Type"),("status","Status"),("serial_number","Serial")],
    detail_groups=[
        {"title":"Asset", "fields":[("name","Name"),("asset_type","Type"),("status","Status")]},
        {"title":"Procurement", "fields":[("serial_number","Serial"),("purchase_date","Purchase Date"),("purchase_cost_kes","Cost (KES)")]},
        {"title":"Ownership", "fields":[("location","Location"),("supplier","Supplier"),("notes","Notes")]},
    ],
)

_task = make_crud(
    model_=Task, form_class_=TaskForm, prefix="core_task",
    search_fields=["title","priority","status","notes"],
    list_columns=[("title","Title"),("priority","Priority"),("status","Status"),("due_date","Due")],
)

LocationList = _location["List"]; LocationDetail = _location["Detail"]; LocationCreate=_location["Create"]; LocationUpdate=_location["Update"]; LocationDelete=_location["Delete"]
SupplierList = _supplier["List"]; SupplierDetail = _supplier["Detail"]; SupplierCreate=_supplier["Create"]; SupplierUpdate=_supplier["Update"]; SupplierDelete=_supplier["Delete"]
PersonList = _person["List"]; PersonDetail = _person["Detail"]; PersonCreate=_person["Create"]; PersonUpdate=_person["Update"]; PersonDelete=_person["Delete"]
AssetList = _asset["List"]; AssetDetail = _asset["Detail"]; AssetCreate=_asset["Create"]; AssetUpdate=_asset["Update"]; AssetDelete=_asset["Delete"]
TaskList = _task["List"]; TaskDetail = _task["Detail"]; TaskCreate=_task["Create"]; TaskUpdate=_task["Update"]; TaskDelete=_task["Delete"]
