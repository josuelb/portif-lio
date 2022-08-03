from rest_framework import serializers
from .models import Comentarios, Conteudos


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = (
            'id',
            'nome', 
            'email', 
            'comentario'
        )


class ConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conteudos
        fields = (
            'id',
            'titulo',
            'link',
            'image',
            'paragrafo',
            'local'
        )