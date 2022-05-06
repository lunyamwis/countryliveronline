from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("", views.view_clients, name="view_clients"),
    path("fetch", views.fetch_clients, name="fetch_clients"),
    path("export", views.export_users_csv, name="export_users_csv"),
]
