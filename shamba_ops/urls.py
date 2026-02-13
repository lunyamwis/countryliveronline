from django.contrib import admin
from django.urls import path, include
from core.views import DashboardView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path("", DashboardView.as_view(), name="dashboard"),

    path("core/", include("core.urls")),
    path("inventory/", include("inventory.urls")),
    path("organic/", include("organic.urls")),
    path("poultry/", include("poultry.urls")),
    path("propagation/", include("propagation.urls")),
    path("nursery/", include("nursery.urls")),
    path("kitchen/", include("kitchen_garden.urls")),
    path("landscaping/", include("landscaping.urls")),
    path("beekeeping/", include("beekeeping.urls")),
    path("repairs/", include("repairs.urls")),
    path("maintenance/", include("maintenance.urls")),
    path("finance/", include("finance.urls")),
]
