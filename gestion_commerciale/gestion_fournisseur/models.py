# models.py
from django.db import models

class Fournisseur(models.Model):
    idfournisseur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numrc = models.CharField(max_length=20, default="Pending")
    i_f  = models.CharField(max_length=20, default="Pending")
    tel = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=15, blank=True)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    date_creation = models.DateField(auto_now=False, editable=True)  # Rendre modifiable
    
    def formatted_date_creation(self):
        return self.date_creation.strftime('%d/%m/%Y')  # Format jj/mm/aaaa

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    class Meta:
        db_table = 'fournisseur'  # Spécifie le nom de la table dans la base de données
        ordering = ['nom']  # Tri par date de création (optionnel)
