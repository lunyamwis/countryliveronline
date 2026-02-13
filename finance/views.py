from core.view_utils import make_crud
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm

_exp = make_crud(
    model_=Expense, form_class_=ExpenseForm, prefix="fin_expense",
    search_fields=["category","description","ref"],
    list_columns=[("date","Date"),("category","Category"),("description","Description"),("amount_kes","Amount (KES)"),("supplier","Supplier")],
)

_inc = make_crud(
    model_=Income, form_class_=IncomeForm, prefix="fin_income",
    search_fields=["source","description","buyer"],
    list_columns=[("date","Date"),("source","Source"),("amount_kes","Amount (KES)"),("buyer","Buyer"),("location","Location")],
)

ExpenseList=_exp["List"]; ExpenseDetail=_exp["Detail"]; ExpenseCreate=_exp["Create"]; ExpenseUpdate=_exp["Update"]; ExpenseDelete=_exp["Delete"]
IncomeList=_inc["List"]; IncomeDetail=_inc["Detail"]; IncomeCreate=_inc["Create"]; IncomeUpdate=_inc["Update"]; IncomeDelete=_inc["Delete"]
