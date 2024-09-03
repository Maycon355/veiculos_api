# veiculos/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Veiculo

class VeiculoTests(APITestCase):

    def test_create_veiculo(self):
        url = reverse('veiculo-list')
        data = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2021}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Outros testes para listar, atualizar e deletar veículos...
    def test_list_veiculos(self):
        url = reverse('veiculo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_update_veiculo(self):
        veiculo = Veiculo.objects.create(marca='Honda', modelo='Civic', ano=2020)
        url = reverse('veiculo-detail', args=[veiculo.id])
        data = {'marca': 'Honda', 'modelo': 'Civic', 'ano': 2021}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_veiculo(self):
        veiculo = Veiculo.objects.create(marca='Honda', modelo='Civic', ano=2020)
        url = reverse('veiculo-detail', args=[veiculo.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

