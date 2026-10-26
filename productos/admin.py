from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'activo', 'creado')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')

