from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from .models import Product
from .serializers import ProductSerializer


class IsAdminJWT(BasePermission):
    def has_permission(self, request, view):
        is_admin = getattr(request.user, 'admin', False)  
        print(f"Usuário {request.user.username} tem admin: {is_admin}")
        return is_admin  


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminJWT]

    def list(self, request, *args, **kwargs):
        is_admin = getattr(request.user, 'admin', False)
        print(f"Permissão de admin para {request.user.username}: {is_admin}")

        if not is_admin:
            return Response({'error': 'Unauthorized: Insufficient permissions'}, status=403)

        return super().list(request, *args, **kwargs)
