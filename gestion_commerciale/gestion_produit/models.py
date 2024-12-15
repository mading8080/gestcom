from django.db import models
import random
import string
from django.core.exceptions import ValidationError


def generer_barcode():
    """Génère un code-barres unique aléatoire de 12 chiffres."""
    return ''.join(random.choices(string.digits, k=12))



class Produit(models.Model):
    idProduit = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Nouveau champ
    
    
    def delete(self, *args, **kwargs):
    # Vérifie si ce produit est lié à des détails de vente
        if self.details_vente.exists():  # Relation inversée via `related_name`
            raise ValidationError("Impossible de supprimer un produit déjà vendu.")
        super().delete(*args, **kwargs)
    

    def __str__(self):
        return self.designation
    
    def save(self, *args, **kwargs):
        # Générer un code-barres unique si absent
        if not self.barcode:
            while True:
                new_barcode = generer_barcode()
                if not Produit.objects.filter(barcode=new_barcode).exists():
                    self.barcode = new_barcode
                    break           
                else: 
                  print(f"Le code-barres est déjà utilisé ")
                      
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'produit'

    def ajuster_stock(self, quantite):
        """Ajuster le stock après vente, quantite peut être négative (retour produit)."""
        self.stock -= quantite
        self.save()


