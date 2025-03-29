import jwt
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model

class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/users/login/', '/users/register/']:  
            return self.get_response(request)


        token = request.headers.get('Authorization')


        if not token:
            return JsonResponse({'error': 'Token is missing'}, status=401)

        if token.startswith('Bearer '):
            token = token[7:]
        

        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            print('\n\n', token, "<--- \n", decoded_token)

            user_id = decoded_token.get('id')
            if not user_id:
                return JsonResponse({'error': 'User ID not found in token'}, status=401)

            User = get_user_model()
            user = User.objects.filter(id=user_id).first()

            if not user:
                return JsonResponse({'error': 'User not found'}, status=401)

            # Atribuir o campo admin ao objeto user apenas se admin for True no token
            if decoded_token.get('admin', False):
                user.admin = True  # Se o token tiver 'admin': True, atribui
            else:
                user.admin = False  # Caso contrário, define como False ou ignora

            request.user = user  # Associar o usuário à requisição

            return self.get_response(request)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)

        return self.get_response(request)
