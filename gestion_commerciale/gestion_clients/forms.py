from django import forms
from .models import Client
from django.utils import timezone
from django.forms import DateInput

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
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
            'date_creation': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    date_creation = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],  # ISO format uniquement
        required=False
    )

    def clean_date_creation(self):
        date_creation = self.cleaned_data.get('date_creation')
        if not date_creation:
            date_creation = timezone.now().date()
        return date_creation

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Client.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Cette adresse email est déjà utilisée.")
        return email

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if tel and not tel.isdigit():
            raise forms.ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
        if tel and Client.objects.filter(tel=tel).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ce numéro de téléphone est déjà utilisé.")
        return tel
