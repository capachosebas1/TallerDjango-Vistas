from django.db import models

from variables.models import Variable

class Measurements(models.Model):
    
    Variable = models.ForeignKey(Variable,on_delete=models.CASCADE,default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit= models.CharField(max_length=50)
    place= models.CharField(max_length=50)
    dataTime= models.DateTimeField(auto_now_add=True)

def __str__(self):
    
    return '%s %s' % (self.value, self.unit)

