from core.forms import BaseBSForm
from .models import Item, StockBatch, StockUsage

class ItemForm(BaseBSForm):
    class Meta: model = Item; fields = "__all__"

class StockBatchForm(BaseBSForm):
    class Meta: model = StockBatch; fields = "__all__"

class StockUsageForm(BaseBSForm):
    class Meta: model = StockUsage; fields = "__all__"
