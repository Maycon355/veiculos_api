# veiculos/models.py

from django.db import models

class Veiculo(models.Model):
    STATUS_CHOICES = [
        ('CONECTADO', 'Conectado'),
        ('DESCONECTADO', 'Desconectado'),
    ]
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='DESCONECTADO')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
