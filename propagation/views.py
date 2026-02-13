from core.view_utils import make_crud
from .models import SeedLot, SeedTreatment, GerminationTest
from .forms import SeedLotForm, SeedTreatmentForm, GerminationTestForm

_lot = make_crud(
    model_=SeedLot, form_class_=SeedLotForm, prefix="prop_seedlot",
    search_fields=["crop_name","variety","lot_code","storage_notes"],
    list_columns=[("crop_name","Crop"),("variety","Variety"),("lot_code","Lot Code"),("expiry_date","Expiry"),("seed_count_est","Seeds")],
)

_treat = make_crud(
    model_=SeedTreatment, form_class_=SeedTreatmentForm, prefix="prop_treatment",
    search_fields=["treatment_type","dosage","notes"],
    list_columns=[("seed_lot","Seed Lot"),("treated_on","Date"),("treatment_type","Treatment"),("dosage","Dosage")],
)

_germ = make_crud(
    model_=GerminationTest, form_class_=GerminationTestForm, prefix="prop_germ",
    search_fields=["medium"],
    list_columns=[("seed_lot","Seed Lot"),("tested_on","Tested"),("sample_size","Sample"),("germinated","Germinated"),("days_to_emerge","Days")],
)

SeedLotList=_lot["List"]; SeedLotDetail=_lot["Detail"]; SeedLotCreate=_lot["Create"]; SeedLotUpdate=_lot["Update"]; SeedLotDelete=_lot["Delete"]
SeedTreatmentList=_treat["List"]; SeedTreatmentDetail=_treat["Detail"]; SeedTreatmentCreate=_treat["Create"]; SeedTreatmentUpdate=_treat["Update"]; SeedTreatmentDelete=_treat["Delete"]
GerminationTestList=_germ["List"]; GerminationTestDetail=_germ["Detail"]; GerminationTestCreate=_germ["Create"]; GerminationTestUpdate=_germ["Update"]; GerminationTestDelete=_germ["Delete"]
