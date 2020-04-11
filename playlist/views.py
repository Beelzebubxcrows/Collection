from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from playlist.models import song
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')


class CreateSong(CreateView):
    model = song
    fields = ['Name','Singer', 'Album', 'Link']


def listsong(request):
    Song = song.objects.all()
    return render(request, 'list.html', {'Song':Song})


def detailsong(request, pk):
    Songg = song.objects.all().filter(pk=pk)
    return render(request, 'details.html', {'Songg':Songg})



class DeleteSong(DeleteView):
    model = song
    success_url = reverse_lazy('list')


class UpdateSong(UpdateView):
    model = song
    fields=['Album', 'Singer', 'Link', 'Name']
    template_name="playlist/song_update.html"
    