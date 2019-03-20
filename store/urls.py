"""GamesStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.views.generic import *
from .models import *
from .views import *


urlpatterns = [
   url(r'^$',
       ListView.as_view(
           queryset=Game.objects.all(),
           context_object_name= 'gameslist',
           template_name='store/gameslist.html'),
       name='gameslist'),

    #SHOPPING BASKET
    url(r'^basket/$',
       ListView.as_view(
           queryset=Comand.objects.all(),
           context_object_name= 'comands',
           template_name='store/shoppingbasket.html'),
       name='shoppingbasket'),

    # URL DETAIL GAME
    url(r'^game/(?P<pk>\d+)/$',
        GameDetail.as_view( ),
        name='gamedetail'),

    #CREATE COMAND
    url(r'^game/(?P<pk>\d+)/add/$',
        addToBasket,
        name='comand'),

    #BUSCADOR
    url(r'^buscador/$',
        buscador,
        name='buscador'),
]
