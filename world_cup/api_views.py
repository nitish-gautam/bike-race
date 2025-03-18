from rest_framework import viewsets, filters
from .models import Team, Rider, QualifyingRaceResult, MainRaceResult
from .serializers import TeamSerializer, RiderSerializer, QualifyingRaceResultSerializer, MainRaceResultSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.select_related('team').all()
    serializer_class = RiderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'team__name']


class QualifyingRaceResultViewSet(viewsets.ModelViewSet):
    queryset = QualifyingRaceResult.objects.select_related('rider').all()
    serializer_class = QualifyingRaceResultSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['qualifying_time']
    ordering = ['qualifying_time']


class MainRaceResultViewSet(viewsets.ModelViewSet):
    queryset = MainRaceResult.objects.select_related('rider').all()
    serializer_class = MainRaceResultSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['finish_time']
    ordering = ['finish_time']
