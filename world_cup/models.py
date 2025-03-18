from django.db import models
from django.core.validators import MinValueValidator


class Team(models.Model):
    """
    Represents a UCI Enduro Team.

    Attributes:
        name (CharField): The unique name of the team.
    """

    name = models.CharField(
        max_length=25,
        unique=True,
        help_text="Name of the team.",
    )

    def __str__(self):
        """
        Returns:
            str: The team's name.
        """
        return self.name


class Rider(models.Model):
    """
    Represents a UCI Enduro Rider.

    Attributes:
        first_name (CharField): Rider's first name.
        last_name (CharField): Rider's last name.
        team (ForeignKey): The team that the rider races for.
        age (PositiveIntegerField): Rider's age in years.
        profile_photo (ImageField): Optional profile photo of the rider.
        race_history (TextField): Optional race history or past race results.
    """

    first_name = models.CharField(
        max_length=20,
        help_text="Rider's first name.",
    )
    last_name = models.CharField(
        max_length=20,
        help_text="Rider's last name.",
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name='riders',
        help_text="Team the rider races for.",
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Rider's age in years.",
    )
    # Extra fields for rider profiles
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        help_text="Optional profile photo of the rider.",
    )
    race_history = models.TextField(
        null=True,
        blank=True,
        help_text="Optional race history of the rider (e.g., past race results).",
    )

    class Meta:
        unique_together = ('first_name', 'last_name')
        ordering = ['last_name', 'first_name']
        verbose_name = "Rider"
        verbose_name_plural = "Riders"

    def __str__(self):
        """
        Returns:
            str: Full name of the rider.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def age_category(self):
        """
        Computes the rider's age category based on their age.

        Returns:
            str: Age category ("Under 12", "Junior", "Senior", or "Veteran").
        """
        if self.age < 12:
            return "Under 12"
        elif 12 <= self.age < 18:
            return "Junior"
        elif 18 <= self.age <= 35:
            return "Senior"
        else:
            return "Veteran"


class QualifyingRaceResult(models.Model):
    """
    Stores the qualifying race result for a rider.

    Attributes:
        rider (OneToOneField): The rider associated with the qualifying result.
        qualifying_time (DurationField): Time taken to complete the qualifying race.
    """

    rider = models.OneToOneField(
        Rider,
        on_delete=models.CASCADE,
        related_name='qualifying_result',
        help_text="The rider's qualifying result.",
    )
    qualifying_time = models.DurationField(
        help_text="Time taken in the qualifying race.",
    )

    class Meta:
        ordering = ['qualifying_time']
        verbose_name = "Qualifying Race Result"
        verbose_name_plural = "Qualifying Race Results"

    def __str__(self):
        """
        Returns:
            str: String representation with the rider's name and qualifying time.
        """
        return f"{self.rider} - {self.qualifying_time}"


class MainRaceResult(models.Model):
    """
    Stores the main race result for a rider.

    Attributes:
        rider (OneToOneField): The rider associated with the main race result.
        finish_time (DurationField): Time taken to complete the main race.
    """

    rider = models.OneToOneField(
        Rider,
        on_delete=models.CASCADE,
        related_name='main_race_result',
        help_text="The rider's main race result.",
    )
    finish_time = models.DurationField(
        help_text="Finish time in the main race.",
    )

    class Meta:
        ordering = ['finish_time']
        verbose_name = "Main Race Result"
        verbose_name_plural = "Main Race Results"

    def __str__(self):
        """
        Returns:
            str: String representation with the rider's name and finish time.
        """
        return f"{self.rider} - {self.finish_time}"
