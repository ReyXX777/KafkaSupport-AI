from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls  # For API documentation
from django.views.generic import TemplateView  # For health check endpoint
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # JWT authentication
from drf_yasg.views import get_schema_view  # Swagger documentation
from drf_yasg import openapi  # Swagger schema
from django.conf import settings  # For serving media files in development
from django.conf.urls.static import static  # For serving static files

# Swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Activity API",
        default_version="v1",
        description="API documentation for Activity Management System",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    # Admin interface URL
    path("admin/", admin.site.urls),

    # API routes for the "activity" app
    path("api/activity/", include("activity.urls")),

    # API documentation endpoints
    path("api/docs/", include_docs_urls(title="Activity API Documentation")),
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    # Health check endpoint
    path("health/", TemplateView.as_view(template_name="health_check.html"), name="health_check"),

    # JWT authentication endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # User management endpoints
    path("api/users/", include("users.urls")),  # Assuming a "users" app exists

    # Kafka integration endpoints
    path("api/kafka/", include("kafka_integration.urls")),  # Assuming a "kafka_integration" app exists
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
