from django.db import models
from measurements.models import Measurements

class Alarms(models.Model):
    name = models.CharField(max_length=50)
    attribute = models.ManyToManyField(Measurements)

def __str__(self):
    return'{}'.format(self.name)

# Create your models here.
