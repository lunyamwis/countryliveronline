from django.urls import path
from . import views

urlpatterns = [
    path("", views.FaultReportList.as_view(), name="rep_fault_list"),

    path("faults/", views.FaultReportList.as_view(), name="rep_fault_list"),
    path("faults/new/", views.FaultReportCreate.as_view(), name="rep_fault_create"),
    path("faults/<int:pk>/", views.FaultReportDetail.as_view(), name="rep_fault_detail"),
    path("faults/<int:pk>/edit/", views.FaultReportUpdate.as_view(), name="rep_fault_update"),
    path("faults/<int:pk>/delete/", views.FaultReportDelete.as_view(), name="rep_fault_delete"),

    path("jobs/", views.RepairJobList.as_view(), name="rep_job_list"),
    path("jobs/new/", views.RepairJobCreate.as_view(), name="rep_job_create"),
    path("jobs/<int:pk>/", views.RepairJobDetail.as_view(), name="rep_job_detail"),
    path("jobs/<int:pk>/edit/", views.RepairJobUpdate.as_view(), name="rep_job_update"),
    path("jobs/<int:pk>/delete/", views.RepairJobDelete.as_view(), name="rep_job_delete"),

    path("parts/", views.RepairPartUsageList.as_view(), name="rep_part_list"),
    path("parts/new/", views.RepairPartUsageCreate.as_view(), name="rep_part_create"),
    path("parts/<int:pk>/", views.RepairPartUsageDetail.as_view(), name="rep_part_detail"),
    path("parts/<int:pk>/edit/", views.RepairPartUsageUpdate.as_view(), name="rep_part_update"),
    path("parts/<int:pk>/delete/", views.RepairPartUsageDelete.as_view(), name="rep_part_delete"),
]
