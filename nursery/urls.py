from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrayBatchList.as_view(), name="nursery_batch_list"),

    path("sites/", views.NurserySiteList.as_view(), name="nursery_site_list"),
    path("sites/new/", views.NurserySiteCreate.as_view(), name="nursery_site_create"),
    path("sites/<int:pk>/", views.NurserySiteDetail.as_view(), name="nursery_site_detail"),
    path("sites/<int:pk>/edit/", views.NurserySiteUpdate.as_view(), name="nursery_site_update"),
    path("sites/<int:pk>/delete/", views.NurserySiteDelete.as_view(), name="nursery_site_delete"),

    path("batches/", views.TrayBatchList.as_view(), name="nursery_batch_list"),
    path("batches/new/", views.TrayBatchCreate.as_view(), name="nursery_batch_create"),
    path("batches/<int:pk>/", views.TrayBatchDetail.as_view(), name="nursery_batch_detail"),
    path("batches/<int:pk>/edit/", views.TrayBatchUpdate.as_view(), name="nursery_batch_update"),
    path("batches/<int:pk>/delete/", views.TrayBatchDelete.as_view(), name="nursery_batch_delete"),

    path("logs/", views.NurseryDailyLogList.as_view(), name="nursery_log_list"),
    path("logs/new/", views.NurseryDailyLogCreate.as_view(), name="nursery_log_create"),
    path("logs/<int:pk>/", views.NurseryDailyLogDetail.as_view(), name="nursery_log_detail"),
    path("logs/<int:pk>/edit/", views.NurseryDailyLogUpdate.as_view(), name="nursery_log_update"),
    path("logs/<int:pk>/delete/", views.NurseryDailyLogDelete.as_view(), name="nursery_log_delete"),

    path("losses/", views.SeedlingLossList.as_view(), name="nursery_loss_list"),
    path("losses/new/", views.SeedlingLossCreate.as_view(), name="nursery_loss_create"),
    path("losses/<int:pk>/", views.SeedlingLossDetail.as_view(), name="nursery_loss_detail"),
    path("losses/<int:pk>/edit/", views.SeedlingLossUpdate.as_view(), name="nursery_loss_update"),
    path("losses/<int:pk>/delete/", views.SeedlingLossDelete.as_view(), name="nursery_loss_delete"),

    path("transplants/", views.TransplantEventList.as_view(), name="nursery_transplant_list"),
    path("transplants/new/", views.TransplantEventCreate.as_view(), name="nursery_transplant_create"),
    path("transplants/<int:pk>/", views.TransplantEventDetail.as_view(), name="nursery_transplant_detail"),
    path("transplants/<int:pk>/edit/", views.TransplantEventUpdate.as_view(), name="nursery_transplant_update"),
    path("transplants/<int:pk>/delete/", views.TransplantEventDelete.as_view(), name="nursery_transplant_delete"),
]
