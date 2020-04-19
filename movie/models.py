from django.db import models
from django.urls import reverse
# Create your models here.
class movies(models.Model):
    user= models.CharField(max_length=100, blank=True)
    Name= models.CharField(blank=False, max_length = 20)
    Year = models.IntegerField(blank=True)
    Genre = models.CharField(blank= False , max_length= 10)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('home',)

