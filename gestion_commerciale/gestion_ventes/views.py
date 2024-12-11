

from django.core.paginator import Paginator
from .models import FactureVente

def liste_factures(request):
    factures = FactureVente.objects.all()
    paginator = Paginator(factures, 10)  # 10 factures par page
    page_number = request.GET.get('page')
    factures_page = paginator.get_page(page_number)
    return render(request, 'gestion_ventes/liste_ventes.html', {'factures': factures_page})


# gestion_ventes/views.py
from django.shortcuts import render, redirect
from .forms import DetailVenteForm

def ajouter_vente(request):
    if request.method == 'POST':
        form = DetailVenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_ventes:liste_factures')
    else:
        form = DetailVenteForm()
    
    return render(request, 'gestion_ventes/ajouter_vente.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import FactureVente
from .forms import FactureVenteForm

def modifier_facture(request, facture_id):
    # Assurez-vous que l'ID est correct
    facture = get_object_or_404(FactureVente, idvente=facture_id)
    
    if request.method == 'POST':
        form = FactureVenteForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('gestion_ventes:liste_factures')  # Redirige vers la liste des factures après la sauvegarde
        else :
            print(form.errors)  # Pour déboguer, afficher les erreurs du formulaire si elles existent
    else:

        form = FactureVenteForm(instance=facture)

    return render(request, 'gestion_ventes/modifier_facture.html', {'form': form})



def supprimer_facture(request,facture_id):
    facture = get_object_or_404(FactureVente, idvente=facture_id)
    facture.delete()  # Supprimer le produit
    return redirect('gestion_ventes:liste_factures')  # Rediriger vers la liste des produits

from django.shortcuts import render, get_object_or_404
from .models import FactureVente, DetailVente
from .forms import DetailVenteForm
from django.http import HttpResponseNotFound

def detail_facture(request, facture_id):
    try:
        facture = FactureVente.objects.get(pk=facture_id)
    except FactureVente.DoesNotExist:
        return HttpResponseNotFound("Facture non trouvée")

    # Récupérer la facture
    facture = get_object_or_404(FactureVente, idvente=facture_id)

    # Récupérer les détails associés à la facture
    details = DetailVente.objects.filter(facture_vente=facture)

    # Calculer le montant total de la facture
    montant_total = sum(detail.montant for detail in details)

    # Mettre à jour le montant total dans le modèle FactureVente
    facture.montant_facture_vente = montant_total
    facture.save()

    #print(f"Montant Total :{montant_total}")
    # Gestion du formulaire d'ajout de détails
    if request.method == "POST":
        form = DetailVenteForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.facture_vente = facture
            detail.save()
        
            # Recalculer le montant total après ajout du détail
            details = DetailVente.objects.filter(facture_vente=facture)  # Récupérer les nouveaux détails
            montant_total = sum(detail.montant for detail in details)
            facture.montant_facture_vente = montant_total  # Mettre à jour le montant total
            facture.save()  # Sauvegarder la facture avec le nouveau montant total
            return redirect('gestion_ventes:detail_facture', facture_id=facture.idvente) 
           
    else:
        form = DetailVenteForm()

    # Passer les informations à la template
    context = {
        'facture': facture,
        'details': details,
        'form': form,
        'montant_total': montant_total,  # Passer le montant total à la template
    }
    return render(request, 'gestion_ventes/facture_detail.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from .forms import DetailVenteForm
from .models import DetailVente

def modifier_detail(request, idDetail_vente):
    detail = get_object_or_404(DetailVente, idDetail_vente=idDetail_vente)

    if request.method == 'POST':
        form = DetailVenteForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('gestion_ventes:detail_facture', facture_id=detail.facture_vente.idvente)
    else:
        form = DetailVenteForm(instance=detail)

    context = {
        'form': form,
        'detail': detail,
    }
    return render(request, 'gestion_ventes/modifier_detail0.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import DetailVente, FactureVente, Produit
from .forms import DetailVenteForm

def ajout_detail_vente(request, facture_id):
    try:
        facture = FactureVente.objects.get(pk=facture_id)
    except FactureVente.DoesNotExist:
        messages.error(request, "La facture de vente n'existe pas.")
        return redirect('factures:list')  # Rediriger vers la liste des factures, par exemple.

    if request.method == 'POST':
        form = DetailVenteForm(request.POST)
        if form.is_valid():
            produit = form.cleaned_data['produit']
            
            # Vérification si le produit existe déjà dans la facture
            if DetailVente.objects.filter(produit=produit, facture_vente=facture).exists():
                # Lever une ValidationError si le produit existe déjà dans la facture
                form.add_error('produit', f"Le produit '{produit.designation}' existe déjà dans cette facture.")
                return render(request, 'gestion_ventes/ajouter_detail_vente.html', {'form': form, 'facture_vente': facture})

            # Si le produit n'existe pas déjà, créer le DetailVente
            form.instance.facture_vente = facture  # Assigner la facture à l'instance
            form.save()
            messages.success(request, "Le détail de vente a été ajouté avec succès.")
            return redirect('gestion_ventes:detail_facture', facture_id=facture_id)

    else:
        form = DetailVenteForm()

    return render(request, 'gestion_ventes/ajouter_detail_vente.html', {'form': form, 'facture_vente': facture})


def supprimer_detail(request, idDetail_vente):
    # Récupérez l'objet DetailVente correspondant
    detail = get_object_or_404(DetailVente, idDetail_vente=idDetail_vente)
    # Récupérez l'ID de la facture associée
    facture_id = detail.facture_vente.idvente
    # Récupérez le produit associé au détail de vente
    produit = detail.produit
    # Ajustez le stock du produit en fonction de la quantité du détail supprimé
    produit.stock += detail.quantite  # On rétablit le stock en ajoutant la quantité
    # Sauvegardez les modifications du produit
    produit.save()
    # Supprimez le détail de la vente
    detail.delete()
    # Redirigez vers la vue de détail de la facture
    return redirect('gestion_ventes:detail_facture', facture_id=facture_id)

from django.http import JsonResponse
from .models import Produit

def get_prix_vente(request):
    produit_id = request.GET.get('produit_id')  # Récupérer l'ID du produit depuis la requête AJAX
    try:
        produit = Produit.objects.get(pk=produit_id)
        return JsonResponse({'prix_vente': produit.prix_vente}, status=200)
    except Produit.DoesNotExist:
        return JsonResponse({'error': 'Produit introuvable'}, status=404)

