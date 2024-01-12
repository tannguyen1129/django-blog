from django.shortcuts import render, redirect, get_object_or_404

from core.models import Category, Blog
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, BlogPostForm, AddUserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url='core:login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    
    return render(request, 'dashboards/dashboard.html', context)

def categories(request):
    return render(request, 'dashboards/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards:categories')
    form = CategoryForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'dashboards/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboards:categories')
    form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'category': category,
    }
    
    return render(request, 'dashboards/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect ('dashboards:categories')


def posts(request):
    posts = Blog.objects.all()
    
    context = {
        'posts':posts,
    } 
    
    return render(request, 'dashboards/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #Temporarily saving the form
            post.author = request.user
            #post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('dashboards:posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'dashboards/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('dashboards:posts')
            
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    
    return render(request, 'dashboards/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect ('dashboards:posts')

def users(request):
    users = User.objects.all()
    
    context = {
        'users': users,
    }
    
    return render(request, 'dashboards/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards:users')
        else:
            print(form.errors)
    form = AddUserForm()
    
    context = {
        'form': form,
    }
    
    
    return render(request, 'dashboards/add_user.html', context)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            return redirect('dashboards:users')
    form = EditUserForm(instance=user)
    
    context = {
        'form': form,
    }
    
    return render(request, 'dashboards/edit_user.html', context)

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('dashboards:users')


