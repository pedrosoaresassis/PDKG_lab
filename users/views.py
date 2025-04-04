from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from datetime import datetime, timedelta  
import jwt
from django.conf import settings
from .serializers import UserSerializer

# =====================================================================================
class RegisterView(APIView):
    permission_classes = [AllowAny] 
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Criação do usuário
            user_data = serializer.validated_data
            is_admin = request.data.get('is_admin', False)  # Aqui você verifica se o campo `is_admin` é fornecido
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=request.data['password']
            )
            
            # Se for um superusuário
            if is_admin:
                user.is_superuser = True
                user.is_admin = True
                user.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================================================================

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
     
        user = authenticate(username=username, password=password)

        if user:
            payload = {
                'id': user.id,
                'username': user.username,
                'admin': user.is_admin,
                'is_staff': user.is_staff,
                'exp': datetime.utcnow() + timedelta(hours=24)
            }
            
            token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
            
            # (opcional) ver o payload decodificado:
            # decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            # print(decoded)

            return Response({'token': token})

        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

# =====================================================================================
class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated] 

    def put(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            user.email = request.data.get('email', user.email)
            new_password = request.data.get('new_password', None)
            if new_password:
                user.set_password(new_password)
            user.save()
            return Response({'message': 'Dados atualizados com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)

# =====================================================================================
class DeleteUserView(APIView):
    def delete(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            user.delete()
            return Response({'message': 'Usuário excluído com sucesso'}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)
    
# =====================================================================================
class ListUsersView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)