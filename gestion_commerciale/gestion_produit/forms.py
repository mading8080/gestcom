# Dans forms.py
from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['idProduit','designation', 'description', 'prix_achat', 'prix_vente', 'stock','barcode']
