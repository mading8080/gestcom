from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils import timezone
from datetime import datetime


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numrc = models.CharField(max_length=20)
    i_f  = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=15,unique=True)
    tel2 = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    #date_creation = models.DateField(default=timezone.now, editable=True)  # Use timezone.now() to get current date
    date_creation = models.DateField(default=now, editable=True)  # Use timezone.now() to get current date
    

    #def formatted_date_creation(self):
    #    return self.date_creation.strftime('%Y/%m/%d')  # Format jj/mm/aaaa

    def clean_date_creation(self):
        date_creation = self.cleaned_data.get('date_creation')
        if not date_creation:
            date_creation = timezone.now().date()  # Date actuelle sans l'heure
        return date_creation

    def save(self, *args, **kwargs):
        # Si la date_creation n'est pas définie (ce qui est improbable avec auto_now_add),
        # nous la définissons à la date actuelle si nécessaire.
        if not self.date_creation:
            self.date_creation = timezone.now().date()

        super().save(*args, **kwargs)  # Appel de la méthode parente

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = 'client'  # Nom de la table dans la base de données
        ordering = ['idclient']  # Tri par date de création (optionnel)



