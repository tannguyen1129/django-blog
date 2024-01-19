
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core import views as CoreView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView, # new
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include("core.urls")),
    path('<slug:slug>/', CoreView.blogs, name='blogs'), 
    
    #Search endpoint
    path('blogs/search/', CoreView.search, name='search'),
    path('dashboard/', include("dashboards.urls")),
    path('learn/', include("learnkhmer.urls")),
    
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",), # new
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)