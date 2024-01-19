
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core import views as CoreView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include("core.urls")),
    path('<slug:slug>/', CoreView.blogs, name='blogs'), 
    
    #Search endpoint
    path('blogs/search/', CoreView.search, name='search'),
    path('dashboard/', include("dashboards.urls")),
    path('learn/', include("learnkhmer.urls")),
    
    path("api-auth/", include("rest_framework.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)