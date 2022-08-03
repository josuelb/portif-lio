from django.urls import path
from .views import *

urlpatterns = [
    path('comentarios/', ComentariosView.as_view(), name='comentarios'),
    path('conteudos/', ConteudoView.as_view(), name='conteudos'),
    path('home/', HomeView.as_view(), name='home'),
    path('tech/', TechView.as_view()),
    path('calc/', CalcView.as_view()),
    path('tech/idroid/', TechView.IdroidView.as_view(), name='idroid'),
    path('calc/supercontador/', CalcView.ContView.as_view(), name='supercontador')
]