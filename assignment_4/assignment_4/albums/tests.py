from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Album

class AlbumTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.album = Album.objects.create(
            title='Test Album',
            owner=self.user
        )

    def test_album_creation(self):
        self.assertEqual(self.album.title, 'Test Album')
        self.assertEqual(str(self.album), 'Test Album')

    def test_album_detail_view(self):
        response = self.client.get(reverse('album_detail', args=[self.album.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album')

    def test_album_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('album_create'), {'title': 'New Album'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Album.objects.count(), 2)
        new_album = Album.objects.get(title='New Album')
        self.assertEqual(new_album.owner, self.user)

    def test_album_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('album_edit', args=[self.album.pk]), {'title': 'Updated Album'})
        self.assertEqual(response.status_code, 302)
        self.album.refresh_from_db()
        self.assertEqual(self.album.title, 'Updated Album')

    def test_memory_upload_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('memory_upload', args=[self.album.pk]), {'caption': 'New Memory'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.album.memory_set.count(), 1)
        new_memory = self.album.memory_set.first()
        self.assertEqual(new_memory.caption, 'New Memory')

