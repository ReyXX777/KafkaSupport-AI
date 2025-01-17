
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls  # For API documentation
from django.views.generic import TemplateView  # For health check endpoint

urlpatterns = [
    # Admin interface URL
    path("admin/", admin.site.urls),

    # API routes for the "activity" app
    path("api/activity/", include("activity.urls")),

    # API documentation endpoint
    path("api/docs/", include_docs_urls(title="Activity API Documentation")),

    # Health check endpoint
    path("health/", TemplateView.as_view(template_name="health_check.html"), name="health_check"),
]
