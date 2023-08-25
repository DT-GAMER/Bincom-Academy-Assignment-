from django.urls import path
from . import views

app_name = 'multimedia'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('profile/<str:username>/', views.view_profile_view, name='view_profile'),
    path('album/create/', views.album_create_view, name='album_create'),
    path('album/edit/<int:album_id>/', views.album_edit_view, name='album_edit'),
    path('album/<int:album_id>/', views.view_album_view, name='view_album'),
    path('album/<int:album_id>/upload/', views.create_memory_view, name='create_memory'),
    path('memory/<int:memory_id>/', views.view_memory_view, name='view_memory'),
    path('memory/<int:memory_id>/edit/', views.memory_edit_view, name='memory_edit'),
    path('memory/<int:memory_id>/comment/', views.post_comment_view, name='post_comment'),
    path('memory/<int:memory_id>/like/', views.like_memory_view, name='like_memory'),
]

