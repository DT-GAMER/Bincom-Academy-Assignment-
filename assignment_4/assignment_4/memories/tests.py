from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Album, Memory

class AlbumModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.album = Album.objects.create(user=self.user, title='Test Album')

    def test_album_creation(self):
        self.assertEqual(self.album.title, 'Test Album')
        self.assertEqual(str(self.album), 'Test Album')

class MemoryModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.album = Album.objects.create(user=self.user, title='Test Album')
        self.memory = Memory.objects.create(album=self.album, title='Test Memory')

    def test_memory_creation(self):
        self.assertEqual(self.memory.title, 'Test Memory')
        self.assertEqual(str(self.memory), 'Test Memory')

class MemoryViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.album = Album.objects.create(user=self.user, title='Test Album')
        self.memory = Memory.objects.create(album=self.album, title='Test Memory')

    def test_memory_upload_view(self):
        url = reverse('memory-upload', args=[self.album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_memory_detail_view(self):
        url = reverse('memory-detail', args=[self.memory.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_like_memory_view(self):
        url = reverse('like-memory', args=[self.memory.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['likes'], 1)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['likes'], 0)

class MemoryTests(MemoryModelTestCase, MemoryViewsTestCase):
    pass

