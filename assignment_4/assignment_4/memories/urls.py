from django.urls import path
from . import views

urlpatterns = [
    path('<int:album_id>/upload/', views.memory_upload, name='memory-upload'),
    path('<int:memory_id>/', views.memory_detail, name='memory-detail'),
    path('<int:memory_id>/like/', views.like_memory, name='like-memory'),
]

