"""
URL configuration for gestion_commerciale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gestion_clients'  # Définit l'espace de noms pour cette application

urlpatterns = [
path('client_list/', views.client_list, name='client_list'),  # Nom de l'URL est 'client_list'
path('ajouter_client/',views.ajouter_client, name='ajouter_client'),  # L'URL recherchée.
path('modifier_client/<int:client_id>/', views.modifier_client, name='modifier_client'),
path('supprimer_client/<int:client_id>/', views.supprimer_client, name='supprimer_client'),
path('', views.page_principal, name='page_principale'),  # URL pour la page principale

    
]
