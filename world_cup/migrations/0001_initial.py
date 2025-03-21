# Generated by Django 5.1.7 on 2025-03-18 15:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Rider's first name", max_length=20)),
                ('last_name', models.CharField(help_text="Rider's last name", max_length=20)),
                ('age', models.PositiveIntegerField(help_text="Rider's age in years", validators=[django.core.validators.MinValueValidator(1)])),
                ('profile_photo', models.ImageField(blank=True, help_text='Profile photo of the rider', null=True, upload_to='profile_photos/')),
                ('race_history', models.TextField(blank=True, help_text='Race history of the rider (e.g., past race results)', null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the team', max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QualifyingRaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifying_time', models.DurationField(help_text='Time taken in the qualifying race')),
                ('rider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='qualifying_result', to='world_cup.rider')),
            ],
            options={
                'ordering': ['qualifying_time'],
            },
        ),
        migrations.CreateModel(
            name='MainRaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_time', models.DurationField(help_text='Finish time in the main race')),
                ('rider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_race_result', to='world_cup.rider')),
            ],
            options={
                'ordering': ['finish_time'],
            },
        ),
        migrations.AddField(
            model_name='rider',
            name='team',
            field=models.ForeignKey(help_text='Team the rider races for', on_delete=django.db.models.deletion.PROTECT, related_name='riders', to='world_cup.team'),
        ),
        migrations.AlterUniqueTogether(
            name='rider',
            unique_together={('first_name', 'last_name')},
        ),
    ]
