from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Payment

User = get_user_model()

class PaymentModelTest(TestCase):
    def setUp(self):
        # User temporario
        self.user = User.objects.create_user(
            username='testeuser',
            email='teste@example.com',
            password='senha123'
        )
        # pagamento teste
        self.payment = Payment.objects.create(
            user=self.user,
            payment_id='PAY123',
            status='pending',
            amount=100.00
        )

    def test_str_method(self):
        #  Verifica o __str__.
        expected_str = f"{self.payment.payment_id} - {self.user.username} - {self.payment.status}"
        self.assertEqual(str(self.payment), expected_str)




    def test_default_status(self):
        # Verifica se o status padrão é 'pending' quando não informado.
        payment = Payment.objects.create(
            user=self.user,
            payment_id='PAY124',
            amount=50.00
        )
        self.assertEqual(payment.status, 'pending')



    def test_unique_payment_id(self):
        # Garante que não seja possível criar dois pagamentos com o mesmo payment_id.
        with self.assertRaises(Exception):
            Payment.objects.create(
                user=self.user,
                payment_id='PAY123',
                amount=200.00
            )
