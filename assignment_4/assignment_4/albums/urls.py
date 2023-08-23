from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.album_create, name='album_create'),
    path('<int:album_id>/', views.album_detail, name='album_detail'),
    path('<int:album_id>/edit/', views.album_edit, name='album_edit'),
    path('<int:album_id>/upload/', views.memory_upload, name='memory_upload'),
]

