from django import forms
from .models import DetailVente, Produit

class DetailVenteForm(forms.ModelForm):
    prix_vente = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        disabled=True,
        label="Prix de vente du produit:"
    )

    class Meta:
        model = DetailVente
        fields = ['produit', 'quantite', 'prix_unitaire']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Désactiver le champ produit en mode modification
        if self.instance and self.instance.pk:
            self.fields['produit'].disabled = True

        # Pré-remplir le prix de vente si un produit est passé
        produit_id = self.data.get('produit') or self.initial.get('produit')
        if produit_id:
            try:
                produit = Produit.objects.get(pk=produit_id)
                print(f"Prix:{produit.prix_vente}")
                self.fields['prix_vente'].initial = produit.prix_vente
            except Produit.DoesNotExist:
                self.fields['prix_vente'].initial = None
        
       
     
           
from django import forms
from .models import FactureVente

class FactureVenteForm(forms.ModelForm):
    class Meta:
        model = FactureVente
        fields = ['client',  'montant_facture_vente', 'date_facture_vente', 'etat_payement']  # Listez ici les champs que vous souhaitez rendre modifiables

