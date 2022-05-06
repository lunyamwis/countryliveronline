from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from marketing.views import email_list_signup
from posts.views import (
    AboutView,
    IndexView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    search,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', index),
    path("", IndexView.as_view(), name="home"),
    # path('blog/', post_list, name='post-list'),
    path("about/", AboutView.as_view(), name="about"),
    path("blog/", PostListView.as_view(), name="post-list"),
    path("search/", search, name="search"),
    path("email-signup/", email_list_signup, name="email-list-signup"),
    # path('create/', post_create, name='post-create'),
    path("create/", PostCreateView.as_view(), name="post-create"),
    # path('post/<id>/', post_detail, name='post-detail'),
    path("post/<pk>/", PostDetailView.as_view(), name="post-detail"),
    # path('post/<id>/update/', post_update, name='post-update'),
    path("post/<pk>/update/", PostUpdateView.as_view(), name="post-update"),
    # path('post/<id>/delete/', post_delete, name='post-delete'),
    path("post/<pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("tinymce/", include("tinymce.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("courses/", include("content.urls")),
    path("shop/", include("shop.urls")),
    path("role/", include("roles.urls", namespace="roles")),
    path("donation/", include("donation.urls", namespace="donation")),
    path("payment/", include("payment.urls")),
    path("payments/", include("payments.urls")),
    path("documentation/", include("documentation.urls", namespace="documentation")),
    path("clients/", include("clients.urls", namespace="clients")),
    path("paypal/", include("paypal.standard.ipn.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
