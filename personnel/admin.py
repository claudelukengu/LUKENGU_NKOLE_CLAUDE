from django.contrib import admin
from .models import Departement, Poste, Employe

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre')

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'departement', 'poste', 'date_embauche')
