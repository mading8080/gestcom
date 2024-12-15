from django.contrib import messages

# Create your views here.
# gestion_fournisseur/views.py
from django.shortcuts import render
from .models import Fournisseur

def index(request):
    return render(request, 'gestion_fournisseur/fournisseurs.html')

# def fournisseur_list(request): peut etre supprimer 

# Exemple de vue pour récupérer et afficher les fournisseurs
from django.shortcuts import render
from .models import Fournisseur  # Assurez-vous d'importer le modèle correct

def fournisseur_list(request):
    # Récupérer tous les fournisseurs
    fournisseurs = Fournisseur.objects.all()  # Assurez-vous que des fournisseurs existent dans la base de données
    return render(request, 'gestion_fournisseur/fournisseurs.html', {'fournisseurs': fournisseurs})


# gestion_fournisseur/views.py
from django.shortcuts import render, redirect
from .models import Fournisseur

def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        print(f'data send: {request.POST}')
        print(request.POST.get('date_creation'))


        if form.is_valid():
            print("Formulaire valide")
            print(form.cleaned_data)
            # Sauvegarder le fournisseur si le formulaire est valide
            fournisseur = form.save(commit=False)
            if not fournisseur.adresse:
                fournisseur.adresse = "Adresse non renseignée"
            if not fournisseur.ville:
                fournisseur.ville = "Ville non renseignée"
            fournisseur.save()
            #form.save()
            # Rediriger vers la liste des fournisseurs ou une autre page après l'ajout réussi
            return redirect('gestion_fournisseur:fournisseur_list')  # Ajustez le nom de l'URL selon votre configuration
        else:
            print("Formulaire invalide")
            print(form.errors)
            # Si le formulaire n'est pas valide, nous afficherons les erreurs
            return render(request, 'gestion_fournisseur/ajouter_fournisseur.html', {'form': form})
    else:
        
        # Si la requête est GET, on crée un formulaire vide
        form = FournisseurForm()
        return render(request, 'gestion_fournisseur/ajouter_fournisseur.html', {'form': form})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Fournisseur
from .forms import FournisseurForm  # Import the form

def modifier_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, idfournisseur=fournisseur_id)

    # Si le formulaire est soumis via POST
    if request.method == 'POST':
        print("Données POST :", request.POST)
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()  # Enregistrer les modifications dans le fournisseur
            return redirect('gestion_fournisseur:fournisseur_list')  # Redirection après sauvegarde
        else:
            print(form.errors)  # Pour déboguer, afficher les erreurs du formulaire si elles existent
    else:
        form = FournisseurForm(instance=fournisseur)

    return render(request, 'gestion_fournisseur/modifier_fournisseur.html', {'form': form, 'fournisseur': fournisseur})

# gestion_fournisseur/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Fournisseur


# Vue pour supprimer un fournisseur
def supprimer_fournisseur(request, fournisseur_id):
  try:  
    fournisseur = get_object_or_404(Fournisseur, idfournisseur=fournisseur_id)
    fournisseur.delete()  # Supprimer le fournisseur de la base de données    
      # Ajouter un message de succès
    messages.success(request, f"Le fournisseur '{fournisseur.nom}' a été supprimé avec succès.")  # Remplacez `fournisseur.nom` par un champ adapté à votre modèle.
  except Exception as e:
        # Ajouter un message d'erreur en cas de problème
        messages.error(request, f"Une erreur est survenue lors de la suppression du Fournisseur : {e}")
  return redirect('gestion_fournisseur:fournisseur_list')  # Rediriger vers la liste des fournisseurs



from django.shortcuts import render

def page_principal(request):
    return render(request, 'page_principal.html')  # Assurez-vous d'avoir un fichier template nommé 'menu_principal.html'



