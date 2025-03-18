from django.views.generic import ListView, TemplateView
from .models import Rider, QualifyingRaceResult, MainRaceResult


class ListRidersView(ListView):
    model = Rider
    template_name = 'world_cup/list_riders.html'
    context_object_name = 'riders'

    def get_queryset(self):
        return super().get_queryset().select_related('team')


class QualifyingResultsView(TemplateView):
    template_name = 'world_cup/qualifying_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qualifying_results'] = QualifyingRaceResult.objects.select_related('rider').order_by('qualifying_time')
        return context


class RaceStartOrderView(TemplateView):
    template_name = 'world_cup/race_start_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = list(QualifyingRaceResult.objects.select_related('rider').order_by('qualifying_time'))
        context['start_order'] = list(reversed(qs))  # Slowest qualifier starts first
        return context


class PodiumView(TemplateView):
    template_name = 'world_cup/podium.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        podiums = {}
        results = MainRaceResult.objects.select_related('rider', 'rider__team').order_by('finish_time')
        for result in results:
            category = result.rider.age_category
            podiums.setdefault(category, []).append(result)
        context['podiums'] = {cat: res[:3] for cat, res in podiums.items()}
        return context
