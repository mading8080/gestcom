from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser  # Si vous utilisez un modèle personnalisé

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Remplacez par `User` si vous n'utilisez pas de modèle personnalisé
        fields = ['username', 'email', 'password1', 'password2', 'role']
