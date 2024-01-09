from django.urls import path, include
from core import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    
]