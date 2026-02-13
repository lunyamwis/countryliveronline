from core.forms import BaseBSForm
from .models import SeedLot, SeedTreatment, GerminationTest
class SeedLotForm(BaseBSForm): 
    class Meta: model=SeedLot; fields="__all__"
class SeedTreatmentForm(BaseBSForm): 
    class Meta: model=SeedTreatment; fields="__all__"
class GerminationTestForm(BaseBSForm): 
    class Meta: model=GerminationTest; fields="__all__"
