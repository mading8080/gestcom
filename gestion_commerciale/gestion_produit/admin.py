

# Register your models here.
from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('idProduit', 'designation', 'prix_achat', 'prix_vente', 'stock', 'barcode')
    search_fields = ('designation', 'barcode')
