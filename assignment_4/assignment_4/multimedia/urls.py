from django.urls import path
from . import views

app_name = 'multimedia'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.edit_profile_view, name='profile'),
    path('change-password/', views.change_password_view, name='change_password'),

    path('albums/', views.album_list_view, name='album_list'),
    path('albums/create/', views.album_create_view, name='album_create'),
    path('albums/<int:album_id>/', views.album_detail_view, name='album_detail'),
    path('albums/<int:album_id>/edit/', views.album_edit_view, name='album_edit'),

    path('memories/<int:memory_id>/', views.memory_detail_view, name='memory_detail'),
    path('memories/<int:memory_id>/edit/', views.memory_edit_view, name='memory_edit'),

    path('search/', views.search_view, name='search'),

    path('password-reset/', views.password_reset_view, name='password_reset'),
    path('password-reset/done/', views.password_reset_done_view, name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('password-reset/complete/', views.password_reset_complete_view, name='password_reset_complete'),
]

