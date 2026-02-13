from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandscapeProjectList.as_view(), name="land_project_list"),

    path("projects/", views.LandscapeProjectList.as_view(), name="land_project_list"),
    path("projects/new/", views.LandscapeProjectCreate.as_view(), name="land_project_create"),
    path("projects/<int:pk>/", views.LandscapeProjectDetail.as_view(), name="land_project_detail"),
    path("projects/<int:pk>/edit/", views.LandscapeProjectUpdate.as_view(), name="land_project_update"),
    path("projects/<int:pk>/delete/", views.LandscapeProjectDelete.as_view(), name="land_project_delete"),

    path("plants/", views.PlantCatalogList.as_view(), name="land_plant_list"),
    path("plants/new/", views.PlantCatalogCreate.as_view(), name="land_plant_create"),
    path("plants/<int:pk>/", views.PlantCatalogDetail.as_view(), name="land_plant_detail"),
    path("plants/<int:pk>/edit/", views.PlantCatalogUpdate.as_view(), name="land_plant_update"),
    path("plants/<int:pk>/delete/", views.PlantCatalogDelete.as_view(), name="land_plant_delete"),

    path("plans/", views.PlantingPlanList.as_view(), name="land_plan_list"),
    path("plans/new/", views.PlantingPlanCreate.as_view(), name="land_plan_create"),
    path("plans/<int:pk>/", views.PlantingPlanDetail.as_view(), name="land_plan_detail"),
    path("plans/<int:pk>/edit/", views.PlantingPlanUpdate.as_view(), name="land_plan_update"),
    path("plans/<int:pk>/delete/", views.PlantingPlanDelete.as_view(), name="land_plan_delete"),

    path("zones/", views.IrrigationZoneList.as_view(), name="land_zone_list"),
    path("zones/new/", views.IrrigationZoneCreate.as_view(), name="land_zone_create"),
    path("zones/<int:pk>/", views.IrrigationZoneDetail.as_view(), name="land_zone_detail"),
    path("zones/<int:pk>/edit/", views.IrrigationZoneUpdate.as_view(), name="land_zone_update"),
    path("zones/<int:pk>/delete/", views.IrrigationZoneDelete.as_view(), name="land_zone_delete"),

    path("workorders/", views.LandscapingWorkOrderList.as_view(), name="land_work_list"),
    path("workorders/new/", views.LandscapingWorkOrderCreate.as_view(), name="land_work_create"),
    path("workorders/<int:pk>/", views.LandscapingWorkOrderDetail.as_view(), name="land_work_detail"),
    path("workorders/<int:pk>/edit/", views.LandscapingWorkOrderUpdate.as_view(), name="land_work_update"),
    path("workorders/<int:pk>/delete/", views.LandscapingWorkOrderDelete.as_view(), name="land_work_delete"),
]
