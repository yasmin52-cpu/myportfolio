from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("api/v1/", include("main.api_urls")),  # Memasang endpoint DRF pada prefix versi 1.
    path("api-auth/", include("rest_framework.urls")),  # Menyediakan login/logout untuk Browsable API.
]