from django.urls import path
from . import views

urlpatterns = [
    path("", views.ItemList.as_view(), name="inventory_item_list"),
    path("items/", views.ItemList.as_view(), name="inventory_item_list"),
    path("items/new/", views.ItemCreate.as_view(), name="inventory_item_create"),
    path("items/<int:pk>/", views.ItemDetail.as_view(), name="inventory_item_detail"),
    path("items/<int:pk>/edit/", views.ItemUpdate.as_view(), name="inventory_item_update"),
    path("items/<int:pk>/delete/", views.ItemDelete.as_view(), name="inventory_item_delete"),

    path("batches/", views.StockBatchList.as_view(), name="inventory_stockbatch_list"),
    path("batches/new/", views.StockBatchCreate.as_view(), name="inventory_stockbatch_create"),
    path("batches/<int:pk>/", views.StockBatchDetail.as_view(), name="inventory_stockbatch_detail"),
    path("batches/<int:pk>/edit/", views.StockBatchUpdate.as_view(), name="inventory_stockbatch_update"),
    path("batches/<int:pk>/delete/", views.StockBatchDelete.as_view(), name="inventory_stockbatch_delete"),

    path("usage/", views.StockUsageList.as_view(), name="inventory_stockusage_list"),
    path("usage/new/", views.StockUsageCreate.as_view(), name="inventory_stockusage_create"),
    path("usage/<int:pk>/", views.StockUsageDetail.as_view(), name="inventory_stockusage_detail"),
    path("usage/<int:pk>/edit/", views.StockUsageUpdate.as_view(), name="inventory_stockusage_update"),
    path("usage/<int:pk>/delete/", views.StockUsageDelete.as_view(), name="inventory_stockusage_delete"),
]
