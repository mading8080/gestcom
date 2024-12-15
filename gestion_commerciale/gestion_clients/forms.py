# gestion_produits/forms.py
from django import forms
from .models import Client
from django.utils import timezone  # Pour obtenir l'heure actuelle
from django.forms import DateInput

class ClientForm(forms.ModelForm):

    
    class Meta:
        model = Client
        fields = '__all__'
       # exclude = ['date_creation']  # Exclure le champ date_creation du formulaire
       # fields = ['nom', 'prenom', 'numrc', 'i_f' , 'email', 'tel', 
       #           'tel2','fax', 'adresse', 'ville']
        # Assurez-vous qu'il n'y a pas de valeur par défaut incorrecte
        numrc = forms.CharField(initial='')
        i_f = forms.CharField(initial='')
        error_messages = {
            'email': {
                'unique': "Cette adresse email est déjà utilisée. Veuillez en choisir une autre.",
            },
             'tel': {
                'unique': "Ce numero de téléphone est déjà utilisée. Veuillez en choisir une autre.",
            },
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'numrc': forms.TextInput(attrs={'class': 'form-control'}),
            'i_f': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'tel2': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),       
            'date_creation': forms.TextInput(attrs={'class': 'form-control'}),           
        }
    date_creation = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%d/%m/%Y'],  # Spécifie le format de date attendu
        required=False  # Optionnel, si vous ne voulez pas que ce champ soit obligatoire
    )

    def clean_date_creation(self):
        # Si la date_creation n'est pas fournie, définir la valeur actuelle
        date_creation = self.cleaned_data.get('date_creation')
        if not date_creation:
            date_creation = timezone.now().date()  # Date actuelle sans l'heure
        return date_creation
    
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

