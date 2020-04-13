from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def register(request):

    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form":form})
