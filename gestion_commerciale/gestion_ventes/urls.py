from django.urls import path
from . import views

app_name = 'gestion_ventes'

urlpatterns = [
    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/modifier/<int:facture_id>/', views.modifier_facture, name='modifier_facture'),    
    path('factures/supprimer/<int:facture_id>/', views.supprimer_facture, name='supprimer_facture'),
    path('factures/detail/<int:facture_id>/', views.detail_facture, name='detail_facture'),
    path('factures/modifier_detail/<int:idDetail_vente>/', views.modifier_detail, name='modifier_detail'),
    path('factures/supprimer_detail/<int:idDetail_vente>/', views.supprimer_detail, name='supprimer_detail'),
    path('factures/ajout_detail_vente/<int:facture_id>/', views.ajout_detail_vente, name='ajout_detail_vente'),
    #path('factures/ajout_detail_vente/<int:facture_id>/', views.ajout_detail_vente, name='ajout_detail_vente'),
    path('get-prix-vente/', views.get_prix_vente, name='get_prix_vente'),    
    
 

]
