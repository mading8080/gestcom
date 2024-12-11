from django.contrib import messages
from django.shortcuts import render
from .models import Produit

def produits_list(request):
    produits_query = Produit.objects.all()  # Récupère tous les produits
    return render(request, 'gestion_produit/produits_liste.html', {'produits': produits_query})


from django.shortcuts import redirect
from .models import Produit

def ajouter_produit(request):
    if request.method == 'POST':
        print('Données Posté:', request.POST)
        # Récupérer les données du formulaire envoyé depuis la modale
        designation = request.POST.get('designation')
        description = request.POST.get('description')
        prix_achat = request.POST.get('prix_achat')
        prix_vente = request.POST.get('prix_vente')
        stock = request.POST.get('stock')
        barcode = request.POST.get('barcode')

        # Créer un nouveau produit
        Produit.objects.create(
            designation=designation,
            description=description,
            prix_achat=prix_achat,
            prix_vente=prix_vente,
            stock=stock,
            barcode=barcode
        )

        # Rediriger vers la liste des produits
        return redirect('gestion_produit:produits_list')

# gestion_produit/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import ProduitForm  # Si vous utilisez un formulaire pour modifier un produit

def modifier_produit(request, Produit_id):
    produit = get_object_or_404(Produit, idProduit=Produit_id)  # Utiliser idproduit au lieu de idProduit
    if request.method == 'POST':
        print("Données POST :", request.POST)
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Le produit a été modifier avec succès.")
            return redirect('gestion_produit:produits_list')  # Rediriger vers la liste des produits
        else:
            messages.error(request, "Une erreur est survenue. Veuillez vérifier les champs.")
    else:

        form = ProduitForm(instance=produit)
    return render(request, 'gestion_produit/modifier_produit.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Produit

def supprimer_produit(request, Produit_id):
    produit = get_object_or_404(Produit, idProduit=Produit_id)
    try:
            produit.delete()
            messages.success(request, "Le produit a été supprimé avec succès.")
            return redirect('gestion_produit:produits_list')  # Redirige vers la liste des produits
    except ValidationError as e:
            messages.error(request, f"Erreur : {str(e)}")
            return redirect('gestion_produit:produits_list')  # Redirige vers la liste des produits



from django.shortcuts import render
from .models import Produit

def recherche_produit(request):
    query = request.GET.get('q', '')  # Récupère le terme de recherche (si présent)
    produits = []

    if query:
        # Recherche les produits qui contiennent la requête dans 'designation' ou 'description'
        produits = Produit.objects.filter(
            designation__icontains=query) | Produit.objects.filter(description__icontains=query)

    return render(request, 'gestion_produit/recherche_produit.html', {
        'produits': produits,
        'query': query
    })

from django.http import JsonResponse
from .models import Produit
import logging

logger = logging.getLogger(__name__)

def recherche_produit2(request):
    try:
        # Récupérer le texte de recherche depuis la requête GET
        query = request.GET.get('query', '').strip()
        logger.info(f"Fonction recherche_produit2 appelée avec query : {query}")
                
        # Si aucune recherche n'est saisie, renvoyer tous les produits
        if not query:
            produits = Produit.objects.all()  # Renvoie tous les produits
        else:
            # Filtrer les produits selon la désignation ou la description
            produits = Produit.objects.filter(
                designation__icontains=query
            ) | Produit.objects.filter(
                description__icontains=query
            )
        
        # Préparer les données à retourner en JSON
        produits_data = produits.values(
            'idProduit', 
            'designation', 
            'description', 
            'prix_achat', 
            'prix_vente', 
            'stock',
            'barcode'
        )
        
        return JsonResponse({'resultats': list(produits_data)})
    
    except Exception as e:
        # Gérer les erreurs et retourner un message d'erreur
        return JsonResponse({'error': str(e)}, status=500)

