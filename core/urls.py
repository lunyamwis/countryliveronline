from django.urls import path
from . import views

urlpatterns = [
    path("locations/", views.LocationList.as_view(), name="core_location_list"),
    path("locations/new/", views.LocationCreate.as_view(), name="core_location_create"),
    path("locations/<int:pk>/", views.LocationDetail.as_view(), name="core_location_detail"),
    path("locations/<int:pk>/edit/", views.LocationUpdate.as_view(), name="core_location_update"),
    path("locations/<int:pk>/delete/", views.LocationDelete.as_view(), name="core_location_delete"),

    path("suppliers/", views.SupplierList.as_view(), name="core_supplier_list"),
    path("suppliers/new/", views.SupplierCreate.as_view(), name="core_supplier_create"),
    path("suppliers/<int:pk>/", views.SupplierDetail.as_view(), name="core_supplier_detail"),
    path("suppliers/<int:pk>/edit/", views.SupplierUpdate.as_view(), name="core_supplier_update"),
    path("suppliers/<int:pk>/delete/", views.SupplierDelete.as_view(), name="core_supplier_delete"),

    path("people/", views.PersonList.as_view(), name="core_person_list"),
    path("people/new/", views.PersonCreate.as_view(), name="core_person_create"),
    path("people/<int:pk>/", views.PersonDetail.as_view(), name="core_person_detail"),
    path("people/<int:pk>/edit/", views.PersonUpdate.as_view(), name="core_person_update"),
    path("people/<int:pk>/delete/", views.PersonDelete.as_view(), name="core_person_delete"),

    path("assets/", views.AssetList.as_view(), name="core_asset_list"),
    path("assets/new/", views.AssetCreate.as_view(), name="core_asset_create"),
    path("assets/<int:pk>/", views.AssetDetail.as_view(), name="core_asset_detail"),
    path("assets/<int:pk>/edit/", views.AssetUpdate.as_view(), name="core_asset_update"),
    path("assets/<int:pk>/delete/", views.AssetDelete.as_view(), name="core_asset_delete"),

    path("tasks/", views.TaskList.as_view(), name="core_task_list"),
    path("tasks/new/", views.TaskCreate.as_view(), name="core_task_create"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="core_task_detail"),
    path("tasks/<int:pk>/edit/", views.TaskUpdate.as_view(), name="core_task_update"),
    path("tasks/<int:pk>/delete/", views.TaskDelete.as_view(), name="core_task_delete"),
]
