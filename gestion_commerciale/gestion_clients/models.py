from django.db import models
from django.core.exceptions import ValidationError


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numrc = models.CharField(max_length=20, default="Pending")
    i_f  = models.CharField(max_length=20, default="Pending")
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    tel = models.CharField(max_length=15,unique=True)
    tel2 = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    date_creation = models.DateField(auto_now=False, editable=True)

    def formatted_date_creation(self):
        return self.date_creation.strftime('%d/%m/%Y')  # Format jj/mm/aaaa

    def save(self, *args, **kwargs):
        # Vérifiez si un client avec les mêmes informations existe déjà
        if Client.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError(f"Un client avec l'email '{self.email}' existe déjà.")
        super().save(*args, **kwargs)  # Appel de la méthode parente

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = 'client'  # Nom de la table dans la base de données
        ordering = ['nom']  # Tri par date de création (optionnel)
