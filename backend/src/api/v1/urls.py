"""URLs for v1"""

from django.urls import include, path

urlpatterns = [
    path("user/", include("users.urls")),
]
