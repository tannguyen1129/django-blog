from django.shortcuts import render, redirect, get_object_or_404

from core.models import Category, Blog, Comment
from information.models import About
from django.db.models import Q
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http import HttpResponseRedirect



def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    try:
        about = About.objects.get()
    except:
        about = None 
    context = {
        'featured_post': featured_post,
        'posts': posts,
        'about':about,
    }
    return render(request, 'core/home.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    #Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments':comments, 
        'comment_count': comment_count, 
    }
    
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published' )
    
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    
    return render(request, 'search.html', context)

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    
    # Use try/except when we want to do some custom action if the category does not exists
    #try:
    #    category = Category.objects.get(pk=category_id)
    #except:
    #    return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
                    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'core/posts_by_category.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()    
        
    context = {
        'form': form,
    }
    
    return render(request, 'core/register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('core:home')
                
    form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'core/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('core:home')





