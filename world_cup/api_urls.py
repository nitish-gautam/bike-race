from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TeamViewSet, RiderViewSet, QualifyingRaceResultViewSet, MainRaceResultViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'riders', RiderViewSet)
router.register(r'qualifying-results', QualifyingRaceResultViewSet)
router.register(r'main-results', MainRaceResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
