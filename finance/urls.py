from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExpenseList.as_view(), name="fin_expense_list"),

    path("expenses/", views.ExpenseList.as_view(), name="fin_expense_list"),
    path("expenses/new/", views.ExpenseCreate.as_view(), name="fin_expense_create"),
    path("expenses/<int:pk>/", views.ExpenseDetail.as_view(), name="fin_expense_detail"),
    path("expenses/<int:pk>/edit/", views.ExpenseUpdate.as_view(), name="fin_expense_update"),
    path("expenses/<int:pk>/delete/", views.ExpenseDelete.as_view(), name="fin_expense_delete"),

    path("income/", views.IncomeList.as_view(), name="fin_income_list"),
    path("income/new/", views.IncomeCreate.as_view(), name="fin_income_create"),
    path("income/<int:pk>/", views.IncomeDetail.as_view(), name="fin_income_detail"),
    path("income/<int:pk>/edit/", views.IncomeUpdate.as_view(), name="fin_income_update"),
    path("income/<int:pk>/delete/", views.IncomeDelete.as_view(), name="fin_income_delete"),
]
