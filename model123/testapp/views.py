from django.shortcuts import render, get_object_or_404, redirect
from testapp.models import Post, Comment,UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .form import AddComment, AddUser, EditProfile, EditPost, AddPost,EditUserProfile
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})


@login_required
def detail(request, id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.all()
    if post.like.filter(id=request.user.id).exists():
        liked = True
    else:
        liked = False

    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail', args=[str(id)]))
    return render(request, 'details.html', {'post': post, 'comments': comment, 'liked': liked, 'form': form})


# Add Post--------
def AddPostView(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'addpost.html', {'form': form})


# Edit Post--------
def EditPostView(request, id):
    post = get_object_or_404(Post, id=id)
    form = EditPost(instance=post)
    if request.method == 'POST':
        form = EditPost(request.POST, instance=post)
        form.save()
        return HttpResponseRedirect(reverse('detail', args=[str(id)]))
    return render(request, 'editform.html', {'form': form})


@login_required
def LikeView(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    print(request.POST.get('post_id'))

    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)

    else:
        post.like.add(request.user)

    return HttpResponseRedirect(reverse('detail', args=[str(id)]))


def SignUpUser(request):
    form = AddUser()
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            return HttpResponse('<h1>Some thing Went Wrong Try to login Once. If not just sign Up again </h1>')

    return render(request, 'registration/signupuser.html', {'form': form})


def ProfileView(request):
    return render(request, 'userprofile.html')

#Update User Profile
def UpdateProfile1(request, id):
    user=UserProfile.objects.get(user_id=id)
    if request.method == 'POST':
        form = EditProfile(request.POST,instance=user)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('<h1> Form is Not Validate. </h1> <h3> Try again  </h3>')
        
    else:
        form=EditProfile(instance=user)
    return render(request, 'updateprofile1.html', {'form': form})

def UpdateProfile(request, id):
    form = EditUserProfile(instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form = EditProfile(request.POST)
            form.save()
        else:
            return HttpResponse('<h1> Form is Not Validate. </h1> <h3> Try again </h3>')
    return render(request, 'updateuser.html', {'form': form})


def DeletePost(request,id):
    post= Post.objects.get(id=id)
    post.delete()
    return redirect('/')

def MyPostView(request):
    post=Post.objects.all()
    return render(request,'mypost.html',{'posts':post})
