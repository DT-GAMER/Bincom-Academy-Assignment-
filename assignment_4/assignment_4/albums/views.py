from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Memory
from .forms import AlbumForm, MemoryForm

@login_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            return redirect('album_detail', album_id=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'templates/album_create.html', {'form': form})

@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    memories = Memory.objects.filter(album=album)
    return render(request, 'templates/album_detail.html', {'album': album, 'memories': memories})

@login_required
def album_edit(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'templates/album_edit.html', {'form': form, 'album': album})

@login_required
def memory_upload(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.album = album
            memory.save()
            return redirect('album_detail', album_id=album.pk)
    else:
        form = MemoryForm()
    return render(request, 'templates/memory_upload.html', {'form': form, 'album': album})

