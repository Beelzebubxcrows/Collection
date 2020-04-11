from django.db import models

# Create your models here.
from django.urls import reverse

class game(models.Model):
    Name = models.CharField(max_length=50, blank= False)
    Genre = models.CharField(max_length=20, blank=False)
    Platform = models.CharField(max_length=20, blank = False)


    def __str__(self):
        return self.Name


    def get_absolute_url(self):

        return reverse("gamelist")