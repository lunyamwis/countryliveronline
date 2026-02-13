from django.urls import path
from . import views

urlpatterns = [
    path("", views.SeedLotList.as_view(), name="prop_seedlot_list"),

    path("lots/", views.SeedLotList.as_view(), name="prop_seedlot_list"),
    path("lots/new/", views.SeedLotCreate.as_view(), name="prop_seedlot_create"),
    path("lots/<int:pk>/", views.SeedLotDetail.as_view(), name="prop_seedlot_detail"),
    path("lots/<int:pk>/edit/", views.SeedLotUpdate.as_view(), name="prop_seedlot_update"),
    path("lots/<int:pk>/delete/", views.SeedLotDelete.as_view(), name="prop_seedlot_delete"),

    path("treatments/", views.SeedTreatmentList.as_view(), name="prop_treatment_list"),
    path("treatments/new/", views.SeedTreatmentCreate.as_view(), name="prop_treatment_create"),
    path("treatments/<int:pk>/", views.SeedTreatmentDetail.as_view(), name="prop_treatment_detail"),
    path("treatments/<int:pk>/edit/", views.SeedTreatmentUpdate.as_view(), name="prop_treatment_update"),
    path("treatments/<int:pk>/delete/", views.SeedTreatmentDelete.as_view(), name="prop_treatment_delete"),

    path("germination/", views.GerminationTestList.as_view(), name="prop_germ_list"),
    path("germination/new/", views.GerminationTestCreate.as_view(), name="prop_germ_create"),
    path("germination/<int:pk>/", views.GerminationTestDetail.as_view(), name="prop_germ_detail"),
    path("germination/<int:pk>/edit/", views.GerminationTestUpdate.as_view(), name="prop_germ_update"),
    path("germination/<int:pk>/delete/", views.GerminationTestDelete.as_view(), name="prop_germ_delete"),
]
