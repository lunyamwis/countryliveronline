from django.urls import path
from . import views

urlpatterns = [
    path("", views.MaintenancePlanList.as_view(), name="maint_plan_list"),

    path("plans/", views.MaintenancePlanList.as_view(), name="maint_plan_list"),
    path("plans/new/", views.MaintenancePlanCreate.as_view(), name="maint_plan_create"),
    path("plans/<int:pk>/", views.MaintenancePlanDetail.as_view(), name="maint_plan_detail"),
    path("plans/<int:pk>/edit/", views.MaintenancePlanUpdate.as_view(), name="maint_plan_update"),
    path("plans/<int:pk>/delete/", views.MaintenancePlanDelete.as_view(), name="maint_plan_delete"),

    path("logs/", views.MaintenanceLogList.as_view(), name="maint_log_list"),
    path("logs/new/", views.MaintenanceLogCreate.as_view(), name="maint_log_create"),
    path("logs/<int:pk>/", views.MaintenanceLogDetail.as_view(), name="maint_log_detail"),
    path("logs/<int:pk>/edit/", views.MaintenanceLogUpdate.as_view(), name="maint_log_update"),
    path("logs/<int:pk>/delete/", views.MaintenanceLogDelete.as_view(), name="maint_log_delete"),
]
