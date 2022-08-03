from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Comentarios, Conteudos
from .serializers import ComentarioSerializer, ConteudoSerializer
from .Automação_de_email import main

"""
APIs
"""


class ConteudoView(APIView):
    def get(self, request):
        conteud = Conteudos.objects.all()
        serializer = ConteudoSerializer(conteud, many=True)
        return Response(serializer.data)


class ComentariosView(APIView):
    def get(self, request):
        comentarios = Comentarios.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        dados = request.data
        serializer = ComentarioSerializer(data=dados)
        serializer.is_valid()
        serializer.save()

        main.enviar_email(to=dados['email'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
Views normais
"""


class HomeView(TemplateView):
    template_name = 'home.html'


class TechView(TemplateView):
    template_name = 'tech/tech.html'

    class IdroidView(TemplateView):
        template_name = 'tech/idroid.html'


class CalcView(TemplateView):
    template_name = 'calc/calc.html'

    class ContView(TemplateView):
        template_name = 'calc/cont/contador.html'
