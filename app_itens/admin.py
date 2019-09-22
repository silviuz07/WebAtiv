from django.contrib import admin
from .models import *

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(IAtaque)
class IAtaqueAdmin(admin.ModelAdmin):
    pass

@admin.register(IDefesa)
class IDefesaAdmin(admin.ModelAdmin):
    pass

@admin.register(IMagico)
class IMagicoAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

