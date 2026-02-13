from django.urls import path
from . import views

urlpatterns = [
    path("", views.GardenBedList.as_view(), name="kitchen_bed_list"),

    path("beds/", views.GardenBedList.as_view(), name="kitchen_bed_list"),
    path("beds/new/", views.GardenBedCreate.as_view(), name="kitchen_bed_create"),
    path("beds/<int:pk>/", views.GardenBedDetail.as_view(), name="kitchen_bed_detail"),
    path("beds/<int:pk>/edit/", views.GardenBedUpdate.as_view(), name="kitchen_bed_update"),
    path("beds/<int:pk>/delete/", views.GardenBedDelete.as_view(), name="kitchen_bed_delete"),

    path("plantings/", views.BedPlantingList.as_view(), name="kitchen_planting_list"),
    path("plantings/new/", views.BedPlantingCreate.as_view(), name="kitchen_planting_create"),
    path("plantings/<int:pk>/", views.BedPlantingDetail.as_view(), name="kitchen_planting_detail"),
    path("plantings/<int:pk>/edit/", views.BedPlantingUpdate.as_view(), name="kitchen_planting_update"),
    path("plantings/<int:pk>/delete/", views.BedPlantingDelete.as_view(), name="kitchen_planting_delete"),

    path("harvests/", views.BedHarvestList.as_view(), name="kitchen_harvest_list"),
    path("harvests/new/", views.BedHarvestCreate.as_view(), name="kitchen_harvest_create"),
    path("harvests/<int:pk>/", views.BedHarvestDetail.as_view(), name="kitchen_harvest_detail"),
    path("harvests/<int:pk>/edit/", views.BedHarvestUpdate.as_view(), name="kitchen_harvest_update"),
    path("harvests/<int:pk>/delete/", views.BedHarvestDelete.as_view(), name="kitchen_harvest_delete"),
]
