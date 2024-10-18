from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TrainingProgramViewSet, CertificationViewSet, 
                    AutomationToolViewSet, KafkaClusterMetricsViewSet)

router = DefaultRouter()
router.register(r'training-programs', TrainingProgramViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'automation-tools', AutomationToolViewSet)
router.register(r'cluster-metrics', KafkaClusterMetricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
