from django.db import models

# Create your models here.
#migrations ko run and t
class About(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=500)

    def __str__(self):
        return self.name


