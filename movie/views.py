from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from movie.models import movies
from django.urls import reverse_lazy
# Create your views here.
class AddMovie(CreateView):
    model = movies
    fields= ['Name', 'Year', "Genre"]
    template_name = 'movie/addmovie.html'



def movielist(request):
    Movie = movies.objects.all()
    return render(request,'movieslist.html',{'Movie':Movie})


def detailmovies(request, pk):
    Moviee = movies.objects.all().filter(pk=pk)
    return render(request,'moviedetails.html',{'Moviee':Moviee})


class DeleteMovie(DeleteView):
    model= movies
   
    success_url = reverse_lazy('movielist')


class UpdateMovie(UpdateView):
    model=movies
    fields= '__all__'
    template_name = 'updatemovies.html'