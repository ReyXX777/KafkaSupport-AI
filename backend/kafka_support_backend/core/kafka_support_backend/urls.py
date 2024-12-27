from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin interface URL
    path("admin/", admin.site.urls),

    # API routes for the "activity" app
    path("api/activity/", include("activity.urls")),
]
