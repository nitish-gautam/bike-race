from django.contrib import admin
from .models import Team, Rider, QualifyingRaceResult, MainRaceResult

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class QualifyingRaceResultInline(admin.StackedInline):
    model = QualifyingRaceResult
    extra = 0

class MainRaceResultInline(admin.StackedInline):
    model = MainRaceResult
    extra = 0

@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'age', 'age_category')
    search_fields = ('first_name', 'last_name', 'team__name')
    list_filter = ('team',)
    inlines = [QualifyingRaceResultInline, MainRaceResultInline]

@admin.register(QualifyingRaceResult)
class QualifyingRaceResultAdmin(admin.ModelAdmin):
    list_display = ('rider', 'qualifying_time')
    search_fields = ('rider__first_name', 'rider__last_name')

@admin.register(MainRaceResult)
class MainRaceResultAdmin(admin.ModelAdmin):
    list_display = ('rider', 'finish_time')
    search_fields = ('rider__first_name', 'rider__last_name')
