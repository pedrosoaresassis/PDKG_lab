from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
