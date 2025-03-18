from django.db import models


class Rider(models.Model):
    """
    Represents a single UCI Enduro Rider.
    """
    first_name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Rider's First name",
    )
    last_name = models.CharField(
        max_length=20,
        unique=True,
        help_text="Rider's Surname",
    )
    team = models.ForeignKey(
        "Team", on_delete=models.PROTECT,
        help_text='Team the Rider races for',
    )
    age = models.PositiveIntegerField(
        help_text="Rider's age in years."
    )

    class Meta:
        unique_together = ('first_name', 'last_name')


class Team(models.Model):
    """
    Represents a single UCI Enduro Team.
    """
    name = models.CharField(
        max_length=25,
        unique=True,
        help_text="Name of the team",
    )
