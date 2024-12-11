# gestion_fournisseur/forms.py
from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['idfournisseur','nom', 'prenom', 'numrc' , 'i_f', 'adresse', 'ville', 'tel', 'tel2', 'fax', 'email', 'date_creation']
        widgets = {
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Forcer l'affichage au format attendu
        if 'instance' in kwargs and kwargs['instance'] and kwargs['instance'].date_creation:
            self.fields['date_creation'].initial = kwargs['instance'].date_creation.strftime('%Y-%m-%d')