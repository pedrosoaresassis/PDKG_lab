from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_id', 'status', 'amount', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']  # Esses campos não podem ser alterados

class PaymentCreateSerializer(serializers.ModelSerializer):
    """Serializer para criar novos pagamentos"""
    
    class Meta:
        model = Payment
        fields = ['payment_id', 'amount', 'status']  # O usuário não precisa passar as datas

    def create(self, validated_data):
        """Criação de pagamento associando ao usuário autenticado"""
        user = self.context['request'].user  # Obtém o usuário logado
        return Payment.objects.create(user=user, **validated_data)
