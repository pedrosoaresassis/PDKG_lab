from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
