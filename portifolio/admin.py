from django.contrib import admin
from .models import Comentarios
# Register your models here.


@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'comentario')
    list_display_links = ('nome', 'email')
    search_fields = ('nome', 'email')
