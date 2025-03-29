from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer

class PaymentListView(generics.ListAPIView):
    """Lista apenas os pagamentos do usuário autenticado."""
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentDetailView(generics.RetrieveAPIView):
    """Exibe detalhes de um pagamento específico do usuário autenticado."""
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user) 


class AdminPaymentListView(generics.ListAPIView):
    """Lista TODOS os pagamentos do sistema (apenas para administradores)."""
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Payment.objects.all()



class PaymentCreateView(generics.CreateAPIView):
    """Endpoint para criar novos pagamentos"""
    serializer_class = PaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Define automaticamente o usuário autenticado"""
        serializer.save(user=self.request.user)