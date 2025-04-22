from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Poste(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True)
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
