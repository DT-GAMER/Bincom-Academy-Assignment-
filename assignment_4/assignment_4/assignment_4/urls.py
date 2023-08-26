from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include URL patterns from each app
    path('', include('multimedia.urls')),
    path('', include('albums.urls')),
    path('', include('memories.urls')),

    # Add a default view for the root URL
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
]
