# app/models.py
from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.IntegerField()
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.especie})"
