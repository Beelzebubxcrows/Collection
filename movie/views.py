from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from movie.models import movies
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.
def userlist(request):

    user= User.objects.all()

    return render(request,"userlist3.html",{"user":user})






class AddMovie(CreateView):
    model = movies
    fields= ['Name', 'Year', "Genre"]
    template_name = 'movie/addmovie.html'



def movielist(request, username):
    try:
        d=movies.objects.get(user="")
        d.user=request.user.username
        d.save()
    except:
        print("list")
    
    Movie = movies.objects.all().filter(user=username)
    if(username==request.user.username):
        return render(request,'movieslist.html',{'Movie':Movie})
    else:
        return render(request,'movieslist2.html',{"Movie":Movie})

def detailmovies(request,username, pk):
    Moviee = movies.objects.all().filter(pk=pk)
    if(username==request.user.username):
        return render(request,'moviedetails.html',{'Moviee':Moviee})
    else:
        return render(request,'moviedetails2.html',{'Moviee':Moviee})
    


class DeleteMovie(DeleteView):
    model= movies
   
    success_url = reverse_lazy('movielist')


class UpdateMovie(UpdateView):
    model=movies
    fields= '__all__'
    template_name = 'updatemovies.html'