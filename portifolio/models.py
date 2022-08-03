from django.db import models

# Create your models here.


class Comentarios(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Conteudos(models.Model):
    local = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    paragrafo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
