from django.urls import path
from . import views

urlpatterns = [
    path("", views.CycleList.as_view(), name="organic_cycle_list"),

    path("plots/", views.PlotList.as_view(), name="organic_plot_list"),
    path("plots/new/", views.PlotCreate.as_view(), name="organic_plot_create"),
    path("plots/<int:pk>/", views.PlotDetail.as_view(), name="organic_plot_detail"),
    path("plots/<int:pk>/edit/", views.PlotUpdate.as_view(), name="organic_plot_update"),
    path("plots/<int:pk>/delete/", views.PlotDelete.as_view(), name="organic_plot_delete"),

    path("crops/", views.CropList.as_view(), name="organic_crop_list"),
    path("crops/new/", views.CropCreate.as_view(), name="organic_crop_create"),
    path("crops/<int:pk>/", views.CropDetail.as_view(), name="organic_crop_detail"),
    path("crops/<int:pk>/edit/", views.CropUpdate.as_view(), name="organic_crop_update"),
    path("crops/<int:pk>/delete/", views.CropDelete.as_view(), name="organic_crop_delete"),

    path("cycles/", views.CycleList.as_view(), name="organic_cycle_list"),
    path("cycles/new/", views.CycleCreate.as_view(), name="organic_cycle_create"),
    path("cycles/<int:pk>/", views.CycleDetail.as_view(), name="organic_cycle_detail"),
    path("cycles/<int:pk>/edit/", views.CycleUpdate.as_view(), name="organic_cycle_update"),
    path("cycles/<int:pk>/delete/", views.CycleDelete.as_view(), name="organic_cycle_delete"),

    path("soiltests/", views.SoilTestList.as_view(), name="organic_soiltest_list"),
    path("soiltests/new/", views.SoilTestCreate.as_view(), name="organic_soiltest_create"),
    path("soiltests/<int:pk>/", views.SoilTestDetail.as_view(), name="organic_soiltest_detail"),
    path("soiltests/<int:pk>/edit/", views.SoilTestUpdate.as_view(), name="organic_soiltest_update"),
    path("soiltests/<int:pk>/delete/", views.SoilTestDelete.as_view(), name="organic_soiltest_delete"),

    path("compost/", views.CompostList.as_view(), name="organic_compost_list"),
    path("compost/new/", views.CompostCreate.as_view(), name="organic_compost_create"),
    path("compost/<int:pk>/", views.CompostDetail.as_view(), name="organic_compost_detail"),
    path("compost/<int:pk>/edit/", views.CompostUpdate.as_view(), name="organic_compost_update"),
    path("compost/<int:pk>/delete/", views.CompostDelete.as_view(), name="organic_compost_delete"),

    path("operations/", views.OperationList.as_view(), name="organic_operation_list"),
    path("operations/new/", views.OperationCreate.as_view(), name="organic_operation_create"),
    path("operations/<int:pk>/", views.OperationDetail.as_view(), name="organic_operation_detail"),
    path("operations/<int:pk>/edit/", views.OperationUpdate.as_view(), name="organic_operation_update"),
    path("operations/<int:pk>/delete/", views.OperationDelete.as_view(), name="organic_operation_delete"),

    path("inputs/", views.InputList.as_view(), name="organic_input_list"),
    path("inputs/new/", views.InputCreate.as_view(), name="organic_input_create"),
    path("inputs/<int:pk>/", views.InputDetail.as_view(), name="organic_input_detail"),
    path("inputs/<int:pk>/edit/", views.InputUpdate.as_view(), name="organic_input_update"),
    path("inputs/<int:pk>/delete/", views.InputDelete.as_view(), name="organic_input_delete"),

    path("pests/", views.PestList.as_view(), name="organic_pest_list"),
    path("pests/new/", views.PestCreate.as_view(), name="organic_pest_create"),
    path("pests/<int:pk>/", views.PestDetail.as_view(), name="organic_pest_detail"),
    path("pests/<int:pk>/edit/", views.PestUpdate.as_view(), name="organic_pest_update"),
    path("pests/<int:pk>/delete/", views.PestDelete.as_view(), name="organic_pest_delete"),

    path("harvests/", views.HarvestList.as_view(), name="organic_harvest_list"),
    path("harvests/new/", views.HarvestCreate.as_view(), name="organic_harvest_create"),
    path("harvests/<int:pk>/", views.HarvestDetail.as_view(), name="organic_harvest_detail"),
    path("harvests/<int:pk>/edit/", views.HarvestUpdate.as_view(), name="organic_harvest_update"),
    path("harvests/<int:pk>/delete/", views.HarvestDelete.as_view(), name="organic_harvest_delete"),
]
