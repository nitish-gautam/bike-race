from django.db import models
from django.core.validators import MinValueValidator


class Team(models.Model):
    """
    Represents a UCI Enduro Team.
    """
    name = models.CharField(
        max_length=25,
        unique=True,
        help_text="Name of the team",
    )

    def __str__(self):
        return self.name


class Rider(models.Model):
    """
    Represents a UCI Enduro Rider.
    """
    first_name = models.CharField(
        max_length=20,
        help_text="Rider's first name",
    )
    last_name = models.CharField(
        max_length=20,
        help_text="Rider's last name",
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name='riders',
        help_text='Team the rider races for',
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Rider's age in years",
    )

    class Meta:
        unique_together = ('first_name', 'last_name')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age_category(self):
        # Define age brackets: Under 18, 18-35, Over 35
        if self.age < 18:
            return "Under 18"
        elif 18 <= self.age <= 35:
            return "Senior"
        else:
            return "Veteran"


class QualifyingRaceResult(models.Model):
    """
    Stores the qualifying race time for each rider.
    """
    rider = models.OneToOneField(
        Rider,
        on_delete=models.CASCADE,
        related_name='qualifying_result'
    )
    qualifying_time = models.DurationField(
        help_text="Time taken in the qualifying race",
    )

    class Meta:
        ordering = ['qualifying_time']

    def __str__(self):
        return f"{self.rider} - {self.qualifying_time}"


class MainRaceResult(models.Model):
    """
    Stores the main race finish time for each rider.
    """
    rider = models.OneToOneField(
        Rider,
        on_delete=models.CASCADE,
        related_name='main_race_result'
    )
    finish_time = models.DurationField(
        help_text="Finish time in the main race",
    )

    class Meta:
        ordering = ['finish_time']

    def __str__(self):
        return f"{self.rider} - {self.finish_time}"
