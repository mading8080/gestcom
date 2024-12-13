from django.shortcuts import render
from gestion_produit import views
from django.contrib.auth.decorators import login_required

@login_required
def page_principale(request):
    return render(request, 'page_principale.html')



def testecamera(request):
    return render(request, 'testecamera.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def enregistrer_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        barcode = data.get('code')
        # Traitez le code-barres ici (par exemple, l'enregistrer dans la base de données)
        print(f"Code-barres scanné : {barcode}")
        return JsonResponse({'message': 'Code-barres reçu'})
    return JsonResponse({'error': 'Mauvaise requête'}, status=400)


from django.shortcuts import render






 