from django.shortcuts import render
from .models import Client
from django.contrib import messages

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gestion_clients/clients_liste.html', {'clients': clients})



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientForm

def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        print('Données Posté:', request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client ajouté avec succès!")
            return redirect('gestion_clients:client_list')
        else:
            # Afficher un message d'erreur si le formulaire n'est pas valide
            
            messages.error(request, "Veuillez vérifier les informations saisies.")
    else:
        form = ClientForm()  # Toujours initialiser un formulaire vide en GET
    
    return render(request, 'gestion_clients/ajouter_client.html', {'form': form})



from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Client
from .forms import ClientForm  # Assurez-vous d'utiliser un formulaire pour les données

def modifier_client(request, client_id):
    client = get_object_or_404(Client, idclient=client_id)  # Définit "client" pour toutes les branches  
    message = None  # Toujours initialiser la variable message
    form = ClientForm(instance=client)  # Initialiser le formulaire avec les données du client

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)  # Mettre à jour le formulaire avec les données POST
        if form.is_valid():
            try:
                # Enregistrez le client avec les données validées
                form.save()
                message = "Client modifié avec succès."  # Message de succès
            except ValidationError as e:
                # Si une validation échoue, on récupère les erreurs et on les affiche
                message = e.message_dict
        else:
            # Si le formulaire n'est pas valide, on peut aussi afficher les erreurs
            message = form.errors
            form = ClientForm(instance=client)

    # Retourner la vue avec le formulaire et le message
    return render(request, 'gestion_clients/modifier_client.html', {
        'form': form,
        'client': client,
        'message': message,  # Toujours passer le message au template
    })


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


