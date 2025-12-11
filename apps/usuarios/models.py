from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PERFIS = ( 
        ('ADMIN', 'Administrador'),
        ('PRODUCAO', 'Gestor de Produção'),
        ('ESTOQUE', 'Estoquista'),
        ('COMPRAS', 'Compras'),
        ('COMERCIAL', 'Comercial'),
        ('DIRETORIA', 'Diretoria'),
        ('DADOS', 'Analista de Dados'),

    )
    perfil = models.CharField(max_length=20,choices=PERFIS)

    