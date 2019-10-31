from django.db import models

# Create your models here.
class Population(models.Model):
    nom = models.CharField(max_length=50)
    nombre_hbitants = models.PositiveIntegerField(default=100000)
    
    def __str__(self):
        return self.nom