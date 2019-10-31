from django.contrib import admin
from .models import Population

# Register your models here.

@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nombre_hbitants','pourcentage')