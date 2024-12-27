from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrainingProgramViewSet, 
    CertificationViewSet, 
    AutomationToolViewSet, 
    KafkaClusterMetricsViewSet
)

# Create a DefaultRouter instance
router = DefaultRouter()

# Register viewsets with the router
router.register(r'training-programs', TrainingProgramViewSet, basename='trainingprogram')
router.register(r'certifications', CertificationViewSet, basename='certification')
router.register(r'automation-tools', AutomationToolViewSet, basename='automationtool')
router.register(r'cluster-metrics', KafkaClusterMetricsViewSet, basename='clustermetrics')

# Define URL patterns
urlpatterns = [
    # Include the router's URLs
    path('', include(router.urls)),
]
