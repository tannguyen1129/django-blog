from django.urls import path, include
from core import views

from .views import BlogList, BlogDetail

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path("api/v1/<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("api/v1/", BlogList.as_view(), name="blog_list"),
    
]