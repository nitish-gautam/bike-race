"""
Tests for the world_cup models.

This test suite verifies the functionality of the Team, Rider, QualifyingRaceResult, 
and MainRaceResult models, ensuring that their string representations and computed properties work as expected.
"""

import pytest
from datetime import timedelta
from django.core.exceptions import ValidationError
from world_cup.models import Team, Rider, QualifyingRaceResult, MainRaceResult


@pytest.mark.django_db
def test_team_str():
    """
    Test the string representation of the Team model.

    This test creates a Team instance and asserts that its string representation matches its name.
    """
    team = Team.objects.create(name="Test Team")
    assert str(team) == "Test Team", "Team string representation should match its name."


@pytest.mark.django_db
def test_rider_age_category():
    """
    Test the computed age_category property of the Rider model.

    This test creates multiple Rider instances with varying ages and verifies that the computed
    age_category returns the expected result for each age bracket.
    """
    team = Team.objects.create(name="Test Team")
    
    # Test Under 12 category
    rider1 = Rider.objects.create(first_name="Child", last_name="Rider", team=team, age=10)
    assert rider1.age_category == "Under 12", "Expected 'Under 12' for age 10"
    
    # Test Junior category (age between 12 and 18)
    rider2 = Rider.objects.create(first_name="Teen", last_name="Rider", team=team, age=15)
    assert rider2.age_category == "Junior", "Expected 'Junior' for age 15"
    
    # Test Senior category (age between 18 and 35)
    rider3 = Rider.objects.create(first_name="Adult", last_name="Rider", team=team, age=25)
    assert rider3.age_category == "Senior", "Expected 'Senior' for age 25"
    
    # Test Veteran category (age greater than 35)
    rider4 = Rider.objects.create(first_name="Old", last_name="Rider", team=team, age=40)
    assert rider4.age_category == "Veteran", "Expected 'Veteran' for age 40"


@pytest.mark.django_db
def test_qualifying_race_result_str():
    """
    Test the string representation of the QualifyingRaceResult model.

    This test creates a Rider and a QualifyingRaceResult with a 5-minute duration (using timedelta).
    It then verifies that the string representation of the qualifying result matches the expected format.
    """
    team = Team.objects.create(name="Test Team")
    rider = Rider.objects.create(first_name="Test", last_name="Rider", team=team, age=20)
    qualifying_result = QualifyingRaceResult.objects.create(
        rider=rider,
        qualifying_time=timedelta(minutes=5)
    )
    expected_str = f"{rider} - 0:05:00"
    assert str(qualifying_result) == expected_str, (
        "QualifyingRaceResult string representation should match the expected format"
    )


@pytest.mark.django_db
def test_main_race_result_str():
    """
    Test the string representation of the MainRaceResult model.

    This test creates a Rider and a MainRaceResult with a finish time of 4 minutes and 30 seconds (using timedelta).
    It then verifies that the string representation of the main race result matches the expected format.
    """
    team = Team.objects.create(name="Test Team")
    rider = Rider.objects.create(first_name="Test", last_name="Rider", team=team, age=20)
    main_result = MainRaceResult.objects.create(
        rider=rider,
        finish_time=timedelta(minutes=4, seconds=30)
    )
    expected_str = f"{rider} - 0:04:30"
    assert str(main_result) == expected_str, (
        "MainRaceResult string representation should match the expected format"
    )
