from django.shortcuts import render
from games.models import game
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.
from django.urls import reverse_lazy



def userlist(request):

    user= User.objects.all()

    return render(request,"userlist2.html",{"user":user})



















def gamelist(request,username):
    try:
        d=game.objects.get(user="")
        d.user=request.user.username
        d.save()
    except:
        print("list")
    Game = game.objects.all().filter(user=username)
    if(username==request.user.username):
        return render(request,'gamelist.html',{'Game':Game})
    else:
        return render(request,'gamelist2.html',{'Game':Game})

class CreateGame(CreateView):
    model = game
    fields=["Name", "Genre", "Platform"]
    template_name= "addgame.html"


def gamedetails(request,username, pk):

    Gamee = game.objects.all().filter(pk=pk)
    if(username==request.user.username):
        return render(request, 'gamedetails.html', {"Gamee":Gamee})
    else:
        return render(request, 'gamedetails2.html', {"Gamee":Gamee})

    

class DeleteGame(DeleteView):
    model= game
   
    success_url = reverse_lazy('gamelist')


class UpdateGame(UpdateView):
    model= game
    fields= '__all__'
    template_name = 'updategame.html'