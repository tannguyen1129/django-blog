
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('<slug:slug>/', BlogsView.blogs, name='blogs'), 
    
    #Search endpoint
    path('blogs/search/', BlogsView.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)