from django.shortcuts import render
from games.models import game
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from django.urls import reverse_lazy
def gamelist(request):
    Game = game.objects.all()

    return render(request,'gamelist.html',{'Game':Game})


class CreateGame(CreateView):
    model = game
    fields="__all__"
    template_name= "addgame.html"


def gamedetails(request, pk):
    Gamee = game.objects.all().filter(pk=pk)
    return render(request, 'gamedetails.html', {"Gamee":Gamee})

class DeleteGame(DeleteView):
    model= game
   
    success_url = reverse_lazy('gamelist')


class UpdateGame(UpdateView):
    model= game
    fields= '__all__'
    template_name = 'updategame.html'