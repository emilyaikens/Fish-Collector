from django.db import models
from django.urls import reverse

#used for dropdown menu
AGE = (
    ('L', 'Larval'),
    ('J', 'Juvenile'),
    ('S', 'Subadult'),
    ('A', 'Adult')
)

class Collector(models.Model):
    name = models.CharField(max_length=50)
    vessel = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collectors_detail', kwargs={'pk': self.id})

class Fish(models.Model):
    commonName = models.CharField(max_length=100)
    sciName = models.CharField(max_length=100)
    habitat = models.TextField(max_length=250)
    quantity = models.IntegerField()

    collectors = models.ManyToManyField(Collector)

#allows us to see the cat name in the admin, rather than CatObject1
    def __str__(self):
        return self.commonName

class Surveys(models.Model):
    date = models.DateField() 
    age = models.CharField(
        max_length=1,
        choices=AGE, #add the choices field option
        default=AGE[3][0] #set default value to A
    )

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_age_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
