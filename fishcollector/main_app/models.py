from django.db import models

# Create your models here.

class Fish(models.Model):
    commonName = models.CharField(max_length=100)
    sciName = models.CharField(max_length=100)
    habitat = models.TextField(max_length=250)
    quantity = models.IntegerField()

#allows us to see the cat name in the admin, rather than CatObject1
    def __str__(self):
        return self.name
