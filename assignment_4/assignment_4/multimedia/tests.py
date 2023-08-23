from django.test import TestCase
from django.urls import reverse
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_login(self):
        response = self.client.post(reverse('user:login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:profile'))

    def test_user_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:login'))

    def test_user_profile_update(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user:profile'), {
            'first_name': 'Updated First Name',
            'last_name': 'Updated Last Name'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:profile'))
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.first_name, 'Updated First Name')
        self.assertEqual(updated_user.last_name, 'Updated Last Name')

    def test_change_password(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user:change_password'), {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:profile'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newtestpassword'))

    def test_create_album(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user:create_album'), {
            'title': 'Test Album',
            'description': 'This is a test album description'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:profile'))
        self.assertTrue(self.user.albums.filter(title='Test Album').exists())

    def test_upload_memory(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user:upload_memory'), {
            'album': self.user.albums.first().id,
            'caption': 'A test memory caption',
            'image': <image_data>,  # Add image data here
            'video': <video_data>,  # Add video data here
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:profile'))
        self.assertTrue(self.user.memories.filter(caption='A test memory caption').exists())

    

