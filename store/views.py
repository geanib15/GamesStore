from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView

from store.models import *


class GameDetail(DetailView):
    model = Game
    template_name = 'store/gamedetail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context


def addToBasket(request, pk):
    game = Game.objects.get(pk=pk)
    comanda = Comand(user=request.user, price=game.price, game=game)
    comanda.save()
    return redirect('store:gamedetail', pk)

def buscador(request):
    resultats = Game.objects.filter(name__contains=request.POST['buscar'])
    dictio = {'resultats': resultats}
    return render(request=request, template_name="store/search.html", context=dictio)
