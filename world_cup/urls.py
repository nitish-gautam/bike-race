from django.urls import path

from world_cup.views import ListRidersView

urlpatterns = [
    path('list-riders/', ListRidersView.as_view(), name='list_riders'),
]
