from django.urls import path
from .views import RegisterView, LoginView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
]