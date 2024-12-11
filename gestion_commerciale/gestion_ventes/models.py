from django.db import models
from gestion_produit.models import Produit  # Importez la classe Produit
from gestion_clients.models import Client


class FactureVente(models.Model):
    # Choix pour l'état de paiement
    ETAT_PAYEMENT_CHOICES = [
        ('Payé', 'Payé'),
        ('Non Payé', 'Non Payé'),
        ('Partiellement Payé', 'Partiellement Payé'),
    ]

    idvente = models.AutoField(primary_key=True)  # auto-increment
    # Ajoutez la clé étrangère vers le modèle Client
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='factures', db_column='id_client')
    date_facture_vente = models.DateField()
    montant_facture_vente = models.DecimalField(max_digits=10, decimal_places=2)
    sold_restant = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    etat_payement = models.CharField(
        max_length=20,
        choices=ETAT_PAYEMENT_CHOICES,
        default='Non Payé'
    )

    def __str__(self):
        return f"Facture #{self.idvente} pour {self.client}"

    class Meta:
        db_table = 'facture_vente'  # Nom de la table dans la base de données
        verbose_name = "Facture de Vente"
        verbose_name_plural = "Factures de Vente"

    
from django.core.exceptions import ValidationError

class DetailVente(models.Model):
    idDetail_vente = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="details_vente")
    facture_vente = models.ForeignKey(FactureVente, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Vérifier si le produit existe déjà dans la même facture
        if DetailVente.objects.filter(produit=self.produit, facture_vente=self.facture_vente).exclude(pk=self.pk).exists():
            raise ValidationError(f"Le produit '{self.produit.designation}' existe déjà dans cette facture.")

        # Calculer le montant de la vente
        self.montant = self.quantite * self.prix_unitaire

        # Ajuster le stock avant de sauvegarder
        if self.pk:  # Si l'objet existe déjà (modification)
            old_quantite = DetailVente.objects.get(pk=self.pk).quantite
            quantite_diff = self.quantite - old_quantite
        else:  # Si c'est un nouvel objet (ajout)
            quantite_diff = self.quantite

        # Ajuster le stock du produit
        self.produit.ajuster_stock(quantite_diff)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Detail vente {self.idDetail_vente} - Produit {self.produit.designation}'

    class Meta:
        db_table = 'detail_vente'
        unique_together = ('produit', 'facture_vente')
