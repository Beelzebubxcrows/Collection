"""playlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from playlist import views
from movie import views as v1
from games import views as v2
from register import views as v4
urlpatterns = [
    url(r'^userr/$', views.userggg),
    path('admin/', admin.site.urls),
       url(r'^register/',v4.register),
    url(r'',include("django.contrib.auth.urls")),
    url(r'^home/$',views.home, name="home"),
    path('addsong/',views.CreateSong.as_view()),
    path('songlists/<username>/', views.listsong, name="list"),
    path('songlist/<username>/<pk>/', views.detailsong),
    url('^delete/(?P<pk>[-\w]+)/$',views.DeleteSong.as_view()),
    url('^update/(?P<pk>[-\w]+)/$',views.UpdateSong.as_view()),
    url('addmovies/',v1.AddMovie.as_view()),
    path('movieslists/<username>/',v1.movielist, name="movielist"),
    path('movieslist/<username>/<pk>/', v1.detailmovies),
     url('^deletemovie/(?P<pk>[-\w]+)/$',v1.DeleteMovie.as_view()),
      url('^updatemovie/(?P<pk>[-\w]+)/$',v1.UpdateMovie.as_view()),
      path('gameslists/<username>/',v2.gamelist, name="gamelist"),
      url('^addgame/$',v2.CreateGame.as_view()),
      path('gameslist/<username>/<pk>/',v2.gamedetails),
       url('^deletegame/(?P<pk>[-\w]+)/$',v2.DeleteGame.as_view()),
      url('^updategame/(?P<pk>[-\w]+)/$',v2.UpdateGame.as_view()),
      url('^people/$',views.userlist),
      url('^peoplegames/$',v2.userlist),
      url('^peoplemovies/$',v1.userlist),
      
      
   
]
