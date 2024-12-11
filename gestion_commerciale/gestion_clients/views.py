from django.shortcuts import render
from .models import Client
from django.contrib import messages

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gestion_clients/clients_liste.html', {'clients': clients})


from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Client


def ajouter_client(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numrc = request.POST.get('numrc')
        i_f = request.POST.get('i_f')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        tel2 = request.POST.get('tel2')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        date_creation = request.POST.get('date_creation')

        # Créer un nouveau client
    #Client.objects.create(
          
        Client = Client(nom=nom, prenom=prenom, numrc=numrc , i_f=i_f , email=email, tel=tel,
            tel2=tel2, adresse=adresse, ville=ville, date_creation=date_creation
        )
        try:
            Client.save()  # Tente d'enregistrer le client
            messages.success(request, "Client ajouté avec succès.")
            return redirect('client_list')  # Redirection après succès
        except ValidationError as e:
            # Capture l'erreur et ajoute le message d'erreur au contexte
            messages.error(request, e.message)  # Ajout d'un message d'erreur
            
    
        
        # Rediriger vers la liste des clients
        return redirect('gestion_clients:client_list')
    
    return render(request, 'gestion_clients/ajouter_client.html')  # Formulaire d'ajout



from django.shortcuts import get_object_or_404, redirect, render
from .models import Client
from .forms import ClientForm

def modifier_client(request, client_id):
    client = get_object_or_404(Client, idclient=client_id)  # Définit "client" pour toutes les branches  
     
     # Si le formulaire est soumis via POST
    if request.method == 'POST':
        print("Données POST :", request.POST)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('gestion_clients:client_list')  # Redirige après modification
        print(form.errors)  # Pour déboguer, afficher les erreurs du formulaire si elles existent
    else:
        form = ClientForm(instance=client)
    return render(request, 'gestion_clients/modifier_client.html', {'form': form , 'Client': client})


from django.shortcuts import get_object_or_404, redirect, render
from .models import  Client

# Vue pour supprimer un fournisseur
def supprimer_client(request, client_id):
    try:
        client = get_object_or_404(Client, idclient=client_id)
        client.delete()  # Supprimer le fournisseur de la base de données
            # Ajouter un message de succès
        messages.success(request, f"Le client '{client.nom}' a été supprimé avec succès.")  # Remplacez `client.nom` par un champ adapté à votre modèle.
    except Exception as e:
        # Ajouter un message d'erreur en cas de problème
        messages.error(request, f"Une erreur est survenue lors de la suppression du client : {e}")

    return redirect('gestion_clients:client_list')  # Rediriger vers la liste des fournisseurs



from django.shortcuts import render

def page_principal(request):
    return render(request, 'page_principal.html')  # Assurez-vous d'avoir un fichier template nommé 'menu_principal.html'


