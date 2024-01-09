from django.shortcuts import render, redirect, get_object_or_404

from core.models import Category, Blog
from django.db.models import Q

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    
    context = {
        'featured_post': featured_post,
        'posts': posts,
    }
    return render(request, 'core/home.html', context)


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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    
    return render(request, 'core/blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published' )
    
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    
    return render(request, 'core/search.html', context)

