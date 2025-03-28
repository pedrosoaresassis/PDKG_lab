from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer


# =====================================================================================
class RegisterView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=request.data['password']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# =====================================================================================
class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        

        user = authenticate(username=username, password=password)
        if  user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
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