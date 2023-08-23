from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory, Comment
from .forms import MemoryForm, CommentForm
from albums.models import Album

@login_required
def memory_upload(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.uploaded_by = request.user
            memory.album = album
            memory.save()
            return redirect('album-detail', album_id=album.id)
    else:
        form = MemoryForm()
    
    context = {'form': form, 'album': album}
    return render(request, 'templates/memory_upload.html', context)

@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    comments = Comment.objects.filter(memory=memory)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.memory = memory
            new_comment.save()
            return redirect('memory-detail', memory_id=memory.id)
    else:
        comment_form = CommentForm()
    
    context = {'memory': memory, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'templates/memory_detail.html', context)

@login_required
def like_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    if request.user in memory.likes.all():
        memory.likes.remove(request.user)
    else:
        memory.likes.add(request.user)
    return redirect('memory-detail', memory_id=memory.id)

