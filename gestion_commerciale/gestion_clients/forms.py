# gestion_produits/forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['date_creation']  # Exclure le champ date_creation du formulaire
        fields = ['nom', 'prenom', 'numrc', 'i_f' , 'email', 'tel', 'tel2', 'adresse', 'ville']
        error_messages = {
            'email': {
                'unique': "Cette adresse email est déjà utilisée. Veuillez en choisir une autre.",
            },
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if email and Client.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(f"Un client avec l'email '{email}' existe déjà.")
        return email
    
    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if tel and Client.objects.filter(tel=tel).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(f"Un client avec le numéro de téléphone '{tel}' existe déjà.")
        return tel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
          # Si vous souhaitez ne pas afficher la date ou la rendre en lecture seule
        #self.fields['date_creation'].disabled = True
        # Forcer l'affichage au format attendu
        #if 'instance' in kwargs and kwargs['instance'] and kwargs['instance'].date_creation:
        #   self.fields['date_creation'].initial = kwargs['instance'].date_creation.strftime('%Y-%m-%d')

