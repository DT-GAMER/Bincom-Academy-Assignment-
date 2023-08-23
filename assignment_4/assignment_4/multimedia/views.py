from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.send_welcome_email()  # Send welcome email to the user
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'templates/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'templates/login.html'm)

def user_logout(request):
    logout(request)pl
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user)
    return render(request, 'templates/profile_edit.html', {'form': form})

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = ChangePasswordForm()
    return render(request, 'templates/change_password.html', {'form': form})

@login_required
def view_profile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'templates/profile_view.html', {'user': user})

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            messages.success(request, 'Album created successfully.')
            return redirect('profile')
    else:
        form = AlbumForm()
    return render(request, 'templates/album_create.html', {'form': form})

@login_required
def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    if album.owner != request.user:
        return redirect('profile')  # Redirect if user doesn't own the album
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'Album updated successfully.')
            return redirect('profile')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'templates/album_edit.html', {'form': form, 'album': album})

@login_required
def create_memory(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.album = album
            memory.save()
            messages.success(request, 'Memory uploaded successfully.')
            return redirect('album_detail', album_id=album_id)
    else:
        form = MemoryForm()
    return render(request, 'templates/memory_upload.html', {'form': form, 'album': album})

@login_required
def view_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    memories = Memory.objects.filter(album=album)
    return render(request, 'templates/album_detail.html', {'album': album, 'memories': memories})

@login_required
def view_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    comments = memory.comments.all()
    comment_form = CommentForm()
    return render(request, 'templates/memory_detail.html', {'memory': memory, 'comments': comments, 'comment_form': comment_form})

@login_required
def edit_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    if memory.owner != request.user:
        return redirect('profile')  # Redirect if user doesn't own the memory
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES, instance=memory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Memory updated successfully.')
            return redirect('memory_detail', memory_id=memory_id)
    else:
        form = MemoryForm(instance=memory)
    return render(request, 'template/memory_edit.html', {'form': form, 'memory': memory})

@login_required
def post_comment(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.memory = memory
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment posted successfully.')
    return redirect('memory_detail', memory_id=memory_id)

@login_required
def like_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    if memory.likes.filter(id=request.user.id).exists():
        memory.likes.remove(request.user)
    else:
        memory.likes.add(request.user)
    return redirect('memory_detail', memory_id=memory_id)



