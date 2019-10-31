from django.shortcuts import render
from .models import Population

# Create your views here.

def home(requests):
    pops = Population.objects.all()
    data = {
        'pops':pops,
    }
    return render(requests, 'index.html', data)
