from django.db import models

class Variable(models.Model):
    name= models.CharField(max_length=50)

    def __str__(sefl):
        return'{}'.format(sefl.name)

# Create your models here.
