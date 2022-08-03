from django.contrib import admin
from .models import Comentarios, Conteudos
# Register your models here.


@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'comentario')
    list_display_links = ('nome', 'email')
    search_fields = ('nome', 'email')


@admin.register(Conteudos)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'paragrafo')
    list_display_links = ('titulo', 'link')
    search_fields = ('titulo', 'link', 'local')