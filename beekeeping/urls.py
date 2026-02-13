from django.urls import path
from . import views

urlpatterns = [
    path("", views.HiveList.as_view(), name="bee_hive_list"),

    path("apiaries/", views.ApiaryList.as_view(), name="bee_apiary_list"),
    path("apiaries/new/", views.ApiaryCreate.as_view(), name="bee_apiary_create"),
    path("apiaries/<int:pk>/", views.ApiaryDetail.as_view(), name="bee_apiary_detail"),
    path("apiaries/<int:pk>/edit/", views.ApiaryUpdate.as_view(), name="bee_apiary_update"),
    path("apiaries/<int:pk>/delete/", views.ApiaryDelete.as_view(), name="bee_apiary_delete"),

    path("hives/", views.HiveList.as_view(), name="bee_hive_list"),
    path("hives/new/", views.HiveCreate.as_view(), name="bee_hive_create"),
    path("hives/<int:pk>/", views.HiveDetail.as_view(), name="bee_hive_detail"),
    path("hives/<int:pk>/edit/", views.HiveUpdate.as_view(), name="bee_hive_update"),
    path("hives/<int:pk>/delete/", views.HiveDelete.as_view(), name="bee_hive_delete"),

    path("inspections/", views.HiveInspectionList.as_view(), name="bee_inspection_list"),
    path("inspections/new/", views.HiveInspectionCreate.as_view(), name="bee_inspection_create"),
    path("inspections/<int:pk>/", views.HiveInspectionDetail.as_view(), name="bee_inspection_detail"),
    path("inspections/<int:pk>/edit/", views.HiveInspectionUpdate.as_view(), name="bee_inspection_update"),
    path("inspections/<int:pk>/delete/", views.HiveInspectionDelete.as_view(), name="bee_inspection_delete"),

    path("feeding/", views.FeedingList.as_view(), name="bee_feeding_list"),
    path("feeding/new/", views.FeedingCreate.as_view(), name="bee_feeding_create"),
    path("feeding/<int:pk>/", views.FeedingDetail.as_view(), name="bee_feeding_detail"),
    path("feeding/<int:pk>/edit/", views.FeedingUpdate.as_view(), name="bee_feeding_update"),
    path("feeding/<int:pk>/delete/", views.FeedingDelete.as_view(), name="bee_feeding_delete"),

    path("harvests/", views.HarvestBatchList.as_view(), name="bee_harvest_list"),
    path("harvests/new/", views.HarvestBatchCreate.as_view(), name="bee_harvest_create"),
    path("harvests/<int:pk>/", views.HarvestBatchDetail.as_view(), name="bee_harvest_detail"),
    path("harvests/<int:pk>/edit/", views.HarvestBatchUpdate.as_view(), name="bee_harvest_update"),
    path("harvests/<int:pk>/delete/", views.HarvestBatchDelete.as_view(), name="bee_harvest_delete"),
]
