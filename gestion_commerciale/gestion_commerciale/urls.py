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
from django.urls import path, include
from gestion_produit.views import ajouter_produit
from gestion_user.views import register  # Importez la vue register depuis gestion_user
from . import views  # Importer la vue principale
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='gestion_user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('gestion_client/', include('gestion_clients.urls')),  # Inclure les URLs de l'application.
    path('gestion_fournisseur/', include('gestion_fournisseur.urls')),  # Inclure les URLs de gestion_fournisseur
    path('gestion_ventes/', include('gestion_ventes.urls')),  # Inclure les URLs de gestion_ventes
    path('gestion_produit/', include('gestion_produit.urls')),  # Inclure les URLs de gestion_ventes
    path('gestion_user/', include('gestion_user.urls')),  # Inclure les URLs de gestion_ventes
    path('', views.page_principale, name='page_principale'),  # Page principale  
    path('testecamera/', views.testecamera, name='testecamera'),
    path('enregistrer_code/', views.enregistrer_code, name='enregistrer_code'),
    #path('ajouter_produit/',ajouter_produit, name='ajouter_produit'),  # L'URL recherchée.
    #path('ventes/', include('gestion_ventes.urls')),  # Gestion des ventes
]
