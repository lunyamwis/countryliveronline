from django.urls import path
from . import views

urlpatterns = [
    path("", views.FlockList.as_view(), name="poultry_flock_list"),

    path("houses/", views.PoultryHouseList.as_view(), name="poultry_house_list"),
    path("houses/new/", views.PoultryHouseCreate.as_view(), name="poultry_house_create"),
    path("houses/<int:pk>/", views.PoultryHouseDetail.as_view(), name="poultry_house_detail"),
    path("houses/<int:pk>/edit/", views.PoultryHouseUpdate.as_view(), name="poultry_house_update"),
    path("houses/<int:pk>/delete/", views.PoultryHouseDelete.as_view(), name="poultry_house_delete"),

    path("flocks/", views.FlockList.as_view(), name="poultry_flock_list"),
    path("flocks/new/", views.FlockCreate.as_view(), name="poultry_flock_create"),
    path("flocks/<int:pk>/", views.FlockDetail.as_view(), name="poultry_flock_detail"),
    path("flocks/<int:pk>/edit/", views.FlockUpdate.as_view(), name="poultry_flock_update"),
    path("flocks/<int:pk>/delete/", views.FlockDelete.as_view(), name="poultry_flock_delete"),

    path("daily/", views.DailyRecordList.as_view(), name="poultry_daily_list"),
    path("daily/new/", views.DailyRecordCreate.as_view(), name="poultry_daily_create"),
    path("daily/<int:pk>/", views.DailyRecordDetail.as_view(), name="poultry_daily_detail"),
    path("daily/<int:pk>/edit/", views.DailyRecordUpdate.as_view(), name="poultry_daily_update"),
    path("daily/<int:pk>/delete/", views.DailyRecordDelete.as_view(), name="poultry_daily_delete"),

    path("feedplans/", views.FeedPlanList.as_view(), name="poultry_feedplan_list"),
    path("feedplans/new/", views.FeedPlanCreate.as_view(), name="poultry_feedplan_create"),
    path("feedplans/<int:pk>/", views.FeedPlanDetail.as_view(), name="poultry_feedplan_detail"),
    path("feedplans/<int:pk>/edit/", views.FeedPlanUpdate.as_view(), name="poultry_feedplan_update"),
    path("feedplans/<int:pk>/delete/", views.FeedPlanDelete.as_view(), name="poultry_feedplan_delete"),

    path("feeding/", views.FeedingEventList.as_view(), name="poultry_feeding_list"),
    path("feeding/new/", views.FeedingEventCreate.as_view(), name="poultry_feeding_create"),
    path("feeding/<int:pk>/", views.FeedingEventDetail.as_view(), name="poultry_feeding_detail"),
    path("feeding/<int:pk>/edit/", views.FeedingEventUpdate.as_view(), name="poultry_feeding_update"),
    path("feeding/<int:pk>/delete/", views.FeedingEventDelete.as_view(), name="poultry_feeding_delete"),

    path("vaccinations/", views.VaccinationList.as_view(), name="poultry_vax_list"),
    path("vaccinations/new/", views.VaccinationCreate.as_view(), name="poultry_vax_create"),
    path("vaccinations/<int:pk>/", views.VaccinationDetail.as_view(), name="poultry_vax_detail"),
    path("vaccinations/<int:pk>/edit/", views.VaccinationUpdate.as_view(), name="poultry_vax_update"),
    path("vaccinations/<int:pk>/delete/", views.VaccinationDelete.as_view(), name="poultry_vax_delete"),

    path("health/", views.HealthIncidentList.as_view(), name="poultry_health_list"),
    path("health/new/", views.HealthIncidentCreate.as_view(), name="poultry_health_create"),
    path("health/<int:pk>/", views.HealthIncidentDetail.as_view(), name="poultry_health_detail"),
    path("health/<int:pk>/edit/", views.HealthIncidentUpdate.as_view(), name="poultry_health_update"),
    path("health/<int:pk>/delete/", views.HealthIncidentDelete.as_view(), name="poultry_health_delete"),

    path("eggs/", views.EggProductionList.as_view(), name="poultry_eggs_list"),
    path("eggs/new/", views.EggProductionCreate.as_view(), name="poultry_eggs_create"),
    path("eggs/<int:pk>/", views.EggProductionDetail.as_view(), name="poultry_eggs_detail"),
    path("eggs/<int:pk>/edit/", views.EggProductionUpdate.as_view(), name="poultry_eggs_update"),
    path("eggs/<int:pk>/delete/", views.EggProductionDelete.as_view(), name="poultry_eggs_delete"),

    path("sales/", views.SalesRecordList.as_view(), name="poultry_sales_list"),
    path("sales/new/", views.SalesRecordCreate.as_view(), name="poultry_sales_create"),
    path("sales/<int:pk>/", views.SalesRecordDetail.as_view(), name="poultry_sales_detail"),
    path("sales/<int:pk>/edit/", views.SalesRecordUpdate.as_view(), name="poultry_sales_update"),
    path("sales/<int:pk>/delete/", views.SalesRecordDelete.as_view(), name="poultry_sales_delete"),
]
