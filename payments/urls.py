from django.urls import path
from .views import PaymentListView, PaymentDetailView, AdminPaymentListView, PaymentCreateView

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='meus_pagamentos'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='detalhe_pagamento'),
    path('admin/payments/', AdminPaymentListView.as_view(), name='admin_payments'),
    path('createpayments/', PaymentCreateView.as_view(), name='criar_pagamento'),
]
