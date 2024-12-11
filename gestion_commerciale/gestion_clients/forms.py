# gestion_produits/forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'numrc', 'i_f' , 'email', 'tel', 'tel2', 'adresse', 'ville', 'date_creation']
        error_messages = {
            'email': {
                'unique': "Cette adresse email est déjà utilisée. Veuillez en choisir une autre.",
            },
        }
        widgets = {
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Un client avec l'email '{email}' existe déjà.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Forcer l'affichage au format attendu
        if 'instance' in kwargs and kwargs['instance'] and kwargs['instance'].date_creation:
            self.fields['date_creation'].initial = kwargs['instance'].date_creation.strftime('%Y-%m-%d')
