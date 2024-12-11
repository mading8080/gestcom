# gestion_fournisseur/urls.py
from django.urls import path
from . import views
app_name = 'gestion_fournisseur'  # Définir le namespace ici

urlpatterns = [
    path('fournisseur_list/', views.fournisseur_list, name='fournisseur_list'),
    path('ajouter_fournisseur/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('modifier_fournisseur/<int:fournisseur_id>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('supprimer_fournisseur/<int:fournisseur_id>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    path('', views.page_principal, name='page_principale'),  # URL pour la page principale
]
