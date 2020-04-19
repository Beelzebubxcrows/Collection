from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from playlist.models import song
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.



def userlist(request):

    user= User.objects.all()

    return render(request,"userlist.html",{"user":user})








def base(request):
    user = User.objects.all().filter(username=request.user.username)
    return render(request,"base.html",{"user":user})




def userggg(request):
    
    
    return render(request,'userk.html',{'User':User})

def home(request):
    return render(request, 'home.html')


class CreateSong(CreateView):
    model = song
    fields = ['Name','Singer', 'Album', 'Link']


def listsong(request,username):
    try:
        d=song.objects.get(user="")
        d.user=request.user.username
        d.save()
    except:
        print("list")

    Song = song.objects.all().filter(user=username)
    if(username == request.user.username):
        return render(request, 'list.html', {'Song':Song})
    else:
        return render(request,'list2.html',{'Song':Song})

def detailsong(request,username, pk):
    Songg = song.objects.all().filter(pk=pk)
    if(username == request.user.username):
        return render(request, 'details.html', {'Songg':Songg})
    else:
        return render(request, 'details1.html', {'Songg':Songg})




class DeleteSong(DeleteView):
    model = song
    success_url = reverse_lazy('list')


class UpdateSong(UpdateView):
    model = song
    fields=['Album', 'Singer', 'Link', 'Name']
    template_name="playlist/song_update.html"
    