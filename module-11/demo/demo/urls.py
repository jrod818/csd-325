# Jose Rodriguez
# 8/2/2026
# Module 11.2 Assignment
# Django Basics

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rodriguez.urls")),
]