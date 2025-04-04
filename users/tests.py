# models.py
from django.test import TestCase
from django.contrib.auth import get_user_model

# views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserModelTest(TestCase):
# --------------------------------------------------------------------------

    def setUp(self):
        self.User = get_user_model()

# --------------------------------------------------------------------------
    def test_create_user(self):
        
        """ cria user comum """
        
        user = self.User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.token = response.data['access']

    
    """ cria user Admin """
    
    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.check_password('adminpass123'))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

# ===================================================================================================================

class UserViewsTest(APITestCase):
# --------------------------------------------------------------------------

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username='adminuser',
            email='adminuser@example.com',
            password='adminpassword'
        )

# --------------------------------------------------------------------------

    def test_register_user(self):

        """Testa o registro de um novo usuário."""

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

# --------------------------------------------------------------------------

    def test_login_user(self):
        
        """Testa o login de um usuário existente."""
        
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        

# --------------------------------------------------------------------------

    def test_update_user(self):
        
        """Testa a atualização dos dados de um usuário autenticado."""
        
        self.client.login(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'updatedemail@example.com',
            'new_password': 'newpassword'
        }
        response = self.client.put(reverse('update-user'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updatedemail@example.com')
        self.assertTrue(self.user.check_password('newpassword'))

# --------------------------------------------------------------------------

    def test_delete_user(self):
        
        """Testa a exclusão de um usuário autenticado."""
        
        self.client.login(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.delete(reverse('delete-user'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(get_user_model().objects.filter(username='testuser').exists())

# --------------------------------------------------------------------------

    def test_list_users(self):
        
        """ Testa a listagem de usuários por um superusuário autenticado. """
        
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.get(reverse('list-users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
