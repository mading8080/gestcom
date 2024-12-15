from django.shortcuts import render
from .models import Client
from django.contrib import messages

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gestion_clients/clients_liste.html', {'clients': clients})




    
"""     
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from .models import Client

def ajouter_client(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numrc = request.POST.get('numrc')
        i_f = request.POST.get('i_f')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        tel = request.POST.get('tel')
        tel2 = request.POST.get('tel2')
        fax = request.POST.get('fax')
        email = request.POST.get('email')
        date_creation = request.POST.get('date_creation')

        try:
            # Création du client
            client = Client(
                nom=nom, prenom=prenom, numrc=numrc, i_f=i_f, adresse=adresse, ville=ville,
                tel=tel, tel2=tel2, fax=fax, email=email, date_creation=date_creation
            )
            client.save()
            messages.success(request, "Client ajouté avec succès.")
            # Aucune redirection ici, on reste dans la même page
            return render(request, 'gestion_clients/clients_liste.html')

        except IntegrityError as e:
            # Gestion des erreurs d'unicité
            print("Erreur d'intégrité : ", e)

            if 'unique constraint' in str(e):
                if 'tel' in str(e):
                    messages.error(request, "Ce numéro de téléphone est déjà utilisé.")
                    print("Erreur : Le numéro de téléphone est déjà utilisé.")
                elif 'email' in str(e):
                    messages.error(request, "Cet email est déjà utilisé.")
                    print("Erreur : L'email est déjà utilisé.")
            else:
                messages.error(request, "Une erreur inattendue s'est produite.")
        
        # Retourner la même page (clients_liste.html) avec les erreurs
        return render(request, 'gestion_clients/clients_liste.html', {
            'form_errors': messages.get_messages(request),
            'nom': nom,
            'prenom': prenom,
            'numrc': numrc,
            'i_f': i_f,
            'adresse': adresse,
            'ville': ville,
            'tel': tel,
            'tel2': tel2,
            'fax': fax,
            'email': email,
            'date_creation': date_creation
        })

    return render(request, 'gestion_clients/clients_liste.html')
"""
# gestion_clients/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        print(f'data send: {request.POST}')
        print(request.POST.get('date_creation'))


        if form.is_valid():
            print("Formulaire valide")
            print(form.cleaned_data)
            # Sauvegarder le client si le formulaire est valide
            client = form.save(commit=False)
            if not client.adresse:
                client.adresse = "Adresse non renseignée"
            if not client.ville:
                client.ville = "Ville non renseignée"
            client.save()
            #form.save()
            # Rediriger vers la liste des clients ou une autre page après l'ajout réussi
            return redirect('gestion_clients:client_list')  # Ajustez le nom de l'URL selon votre configuration
        else:
            print("Formulaire invalide")
            print(form.errors)
            # Si le formulaire n'est pas valide, nous afficherons les erreurs
            return render(request, 'gestion_clients/ajouter_client.html', {'form': form})
    else:
        
        # Si la requête est GET, on crée un formulaire vide
        form = ClientForm()
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
              
                cleaned_date = form.cleaned_data['date_creation']
                # Enregistrez le client avec les données validées
                form.save()
                message = "Client modifié avec succès."  # Message de succès

                # Redirigez vers la liste des clients après une modification réussie
                return redirect('gestion_clients:client_list')  # Remplacez par l'URL de votre page de liste
            
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


