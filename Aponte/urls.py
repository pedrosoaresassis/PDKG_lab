from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),  # URLs para o app 'users'
    path('products/', include('products.urls')),  # URLs para o app 'products'
    path('payments/', include('payments.urls')),  # URLs para o app 'payments'
]
