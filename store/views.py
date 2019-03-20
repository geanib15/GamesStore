from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from store.models import *


class GameDetail(DetailView):
    model = Game
    template_name = 'store/gamedetail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context