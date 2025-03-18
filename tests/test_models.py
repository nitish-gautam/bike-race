import pytest
from datetime import timedelta
from django.core.exceptions import ValidationError
from world_cup.models import Team, Rider, QualifyingRaceResult, MainRaceResult


@pytest.mark.django_db
def test_team_str():
    """
    Test the string representation of the Team model.
    """
    team = Team.objects.create(name="Test Team")
    assert str(team) == "Test Team"


@pytest.mark.django_db
def test_rider_age_category():
    """
    Test the computed age_category property of the Rider model.
    """
    team = Team.objects.create(name="Test Team")
    
    # Test Under 12 category
    rider1 = Rider.objects.create(first_name="Child", last_name="Rider", team=team, age=10)
    assert rider1.age_category == "Under 12"
    
    # Test Junior category (age between 12 and 18)
    rider2 = Rider.objects.create(first_name="Teen", last_name="Rider", team=team, age=15)
    assert rider2.age_category == "Junior"
    
    # Test Senior category (age between 18 and 35)
    rider3 = Rider.objects.create(first_name="Adult", last_name="Rider", team=team, age=25)
    assert rider3.age_category == "Senior"
    
    # Test Veteran category (age greater than 35)
    rider4 = Rider.objects.create(first_name="Old", last_name="Rider", team=team, age=40)
    assert rider4.age_category == "Veteran"


@pytest.mark.django_db
def test_qualifying_race_result_str():
    """
    Test the string representation of the QualifyingRaceResult model.
    """
    team = Team.objects.create(name="Test Team")
    rider = Rider.objects.create(first_name="Test", last_name="Rider", team=team, age=20)
    # Create a qualifying result with a 5-minute time duration using a timedelta
    qualifying_result = QualifyingRaceResult.objects.create(
        rider=rider, qualifying_time=timedelta(minutes=5)
    )
    
    expected_str = f"{rider} - 0:05:00"
    assert str(qualifying_result) == expected_str


@pytest.mark.django_db
def test_main_race_result_str():
    """
    Test the string representation of the MainRaceResult model.
    """
    team = Team.objects.create(name="Test Team")
    rider = Rider.objects.create(first_name="Test", last_name="Rider", team=team, age=20)
    # Create a main race result with a 4-minute, 30-second finish time using a timedelta
    main_result = MainRaceResult.objects.create(
        rider=rider, finish_time=timedelta(minutes=4, seconds=30)
    )
    
    expected_str = f"{rider} - 0:04:30"
    assert str(main_result) == expected_str
