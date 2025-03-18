from django.urls import path
from .views import ListRidersView, QualifyingResultsView, RaceStartOrderView, PodiumView

urlpatterns = [
    path('list-riders/', ListRidersView.as_view(), name='list_riders'),
    path('qualifying-results/', QualifyingResultsView.as_view(), name='qualifying_results'),
    path('race-start-order/', RaceStartOrderView.as_view(), name='race_start_order'),
    path('podium/', PodiumView.as_view(), name='podium'),
]
