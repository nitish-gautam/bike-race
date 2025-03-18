from rest_framework import serializers
from .models import Team, Rider, QualifyingRaceResult, MainRaceResult


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class RiderSerializer(serializers.ModelSerializer):
    age_category = serializers.ReadOnlyField()

    class Meta:
        model = Rider
        fields = ['id', 'first_name', 'last_name', 'team', 'age', 'age_category']


class QualifyingRaceResultSerializer(serializers.ModelSerializer):
    rider = RiderSerializer(read_only=True)
    rider_id = serializers.PrimaryKeyRelatedField(queryset=Rider.objects.all(), source='rider', write_only=True)

    class Meta:
        model = QualifyingRaceResult
        fields = ['id', 'rider', 'rider_id', 'qualifying_time']


class MainRaceResultSerializer(serializers.ModelSerializer):
    rider = RiderSerializer(read_only=True)
    rider_id = serializers.PrimaryKeyRelatedField(queryset=Rider.objects.all(), source='rider', write_only=True)

    class Meta:
        model = MainRaceResult
        fields = ['id', 'rider', 'rider_id', 'finish_time']
