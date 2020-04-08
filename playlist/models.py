from django.db import models
from django.urls import reverse
# Create your models here.
class song(models.Model):
    Name = models.CharField(max_length=20, blank = False)
    Singer = models.CharField(max_length=15, blank = False)
    Album = models.CharField(max_length=15, blank= True)
    Link = models.URLField(blank=False)


    def __str__(self):
        return self.Name


    def get_absolute_url(self):
        return reverse('list',)

