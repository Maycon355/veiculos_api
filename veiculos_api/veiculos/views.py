# veiculos/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Veiculo
from .serializers import VeiculoSerializer
from rest_framework.decorators import action

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    # Endpoint para atualizar o status do veículo
    @action(detail=True, methods=['put'])
    def atualizar_status(self, request, pk=None):
        veiculo = self.get_object()
        status = request.data.get('status')

        if status not in dict(Veiculo.STATUS_CHOICES):
            return Response({'error': 'Status inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        veiculo.status = status
        veiculo.save()
        return Response({'status': 'Status atualizado com sucesso.'})
