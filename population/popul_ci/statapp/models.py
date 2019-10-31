from django.db import models
from django.db.models import Avg, Max, Min, Sum

# Create your models here.
class Population(models.Model):
    nom = models.CharField(max_length=50)
    nombre_hbitants = models.PositiveIntegerField(default=100000)
    
    def __str__(self):
      return self.nom
    
    @property
    def pourcentage(self):
       total = Population.objects.all().aggregate(ma_sum = Sum('nombre_hbitants'))
       pourcent = (self.nombre_hbitants/total['ma_sum'] )*100
       return round(pourcent, 2)
        
    
   