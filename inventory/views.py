from core.view_utils import make_crud
from .models import Item, StockBatch, StockUsage
from .forms import ItemForm, StockBatchForm, StockUsageForm

_item = make_crud(
    model_=Item, form_class_=ItemForm, prefix="inventory_item",
    search_fields=["name","category","unit","notes"],
    list_columns=[("name","Item"),("category","Category"),("unit","Unit"),("reorder_level","Reorder Level")],
)

_batch = make_crud(
    model_=StockBatch, form_class_=StockBatchForm, prefix="inventory_stockbatch",
    search_fields=["batch_code"],
    list_columns=[("item","Item"),("batch_code","Batch"),("received_date","Received"),("expiry_date","Expiry"),("qty_remaining","Remaining")],
)

_usage = make_crud(
    model_=StockUsage, form_class_=StockUsageForm, prefix="inventory_stockusage",
    search_fields=["purpose"],
    list_columns=[("item","Item"),("location","Location"),("used_on","Used On"),("qty_used","Qty"),("purpose","Purpose")],
)

ItemList=_item["List"]; ItemDetail=_item["Detail"]; ItemCreate=_item["Create"]; ItemUpdate=_item["Update"]; ItemDelete=_item["Delete"]
StockBatchList=_batch["List"]; StockBatchDetail=_batch["Detail"]; StockBatchCreate=_batch["Create"]; StockBatchUpdate=_batch["Update"]; StockBatchDelete=_batch["Delete"]
StockUsageList=_usage["List"]; StockUsageDetail=_usage["Detail"]; StockUsageCreate=_usage["Create"]; StockUsageUpdate=_usage["Update"]; StockUsageDelete=_usage["Delete"]
