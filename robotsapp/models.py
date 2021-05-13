from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_da_empresa = models.CharField(max_length=500)
    cnpj = models.CharField(max_length=30, unique=True)
    data_de_cadastro = models.DateField()

    def __str__(self):
        return self.nome_da_empresa

class Usuario(AbstractUser):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

class Robo(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    campo1 = models.TextField()
    campo2 = models.TextField()
    campo3 = models.TextField()