from core.forms import BaseBSForm
from .models import Expense, Income
class ExpenseForm(BaseBSForm): 
    class Meta: model=Expense; fields="__all__"
class IncomeForm(BaseBSForm): 
    class Meta: model=Income; fields="__all__"
