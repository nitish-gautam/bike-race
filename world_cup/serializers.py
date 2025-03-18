from rest_framework import serializers
from .models import Team, Rider, QualifyingRaceResult, MainRaceResult


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model.

    This serializer provides the fields necessary to create, update, and retrieve Team instances.
    """

    class Meta:
        model = Team
        fields = ['id', 'name']


class RiderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rider model.

    This serializer includes all relevant fields for a Rider along with a read-only field for the computed age category.
    """
    age_category = serializers.ReadOnlyField()

    class Meta:
        model = Rider
        fields = ['id', 'first_name', 'last_name', 'team', 'age', 'age_category']


class QualifyingRaceResultSerializer(serializers.ModelSerializer):
    """
    Serializer for the QualifyingRaceResult model.

    This serializer nests the RiderSerializer (read-only) for display purposes,
    and provides a separate write-only field 'rider_id' to associate a qualifying result with a rider.
    """
    rider = RiderSerializer(read_only=True)
    rider_id = serializers.PrimaryKeyRelatedField(
        queryset=Rider.objects.all(), source='rider', write_only=True
    )

    class Meta:
        model = QualifyingRaceResult
        fields = ['id', 'rider', 'rider_id', 'qualifying_time']


class MainRaceResultSerializer(serializers.ModelSerializer):
    """
    Serializer for the MainRaceResult model.

    Similar to QualifyingRaceResultSerializer, this serializer nests the RiderSerializer (read-only)
    and uses a write-only field 'rider_id' to assign the associated rider.
    """
    rider = RiderSerializer(read_only=True)
    rider_id = serializers.PrimaryKeyRelatedField(
        queryset=Rider.objects.all(), source='rider', write_only=True
    )

    class Meta:
        model = MainRaceResult
        fields = ['id', 'rider', 'rider_id', 'finish_time']
