from django.views import generic

from world_cup.models import Rider


class ListRidersView(generic.ListView):
    model = Rider
    template_name = 'world_cup/list_riders.html'
