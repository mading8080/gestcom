# gestion_fournisseur/urls.py



from django.urls import path
from . import views

app_name = 'gestion_produit'  # Définit le namespace pour cette application

urlpatterns = [
    path('produits_list/', views.produits_list, name='produits_list'),
    path('modifier_produit/<int:Produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),  # Assurez-vous que cette route est présente
    path('supprimer_produit/<int:Produit_id>/', views.supprimer_produit, name='supprimer_produit'),  # Définition de l'URL pour supprimer un produit
    path('recherche_produit/', views.recherche_produit, name='recherche_produit'),
    path('recherche/', views.recherche_produit2, name='recherche_produit2'),
]