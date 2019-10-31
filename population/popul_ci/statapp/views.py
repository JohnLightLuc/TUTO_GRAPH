from django.shortcuts import render
from . import models
from django.db.models import Avg, Max, Min

# Create your views here.

def home(requests):
    pops = models.Population.objects.all().order_by('-nombre_hbitants')
    data = {
        'pops':pops,
    }
    return render(requests, 'index.html', data)

def statistique(requests):
    pops = models.Population.objects.all().order_by('nombre_hbitants')
    moy = models.Population.objects.all().aggregate(moyenne =Avg('nombre_hbitants'))
    maxi = models.Population.objects.all().aggregate(maximun = Max('nombre_hbitants'))
    mini = models.Population.objects.all().aggregate(minimun = Min('nombre_hbitants'))
    pop_max = models.Population.objects.all().filter(nombre_hbitants= maxi['maximun'] )
    pop_min = models.Population.objects.all().filter(nombre_hbitants= mini['minimun'] )
   

    data = {
        'pops':pops,
        'moy':moy,
        'maxi':maxi,
        'mini':mini,
    }
    return render(requests, 'statistique.html', data)
