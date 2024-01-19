from django.urls import path, include
from core import views

from .views import BlogList, BlogDetail, UserList, UserDetail

app_name = 'core'

from rest_framework.routers import SimpleRouter
from .views import UserViewSet, BlogViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", BlogViewSet, basename="blogs")

urlpatterns = router.urls

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path("api/v1/<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("api/v1/", BlogList.as_view(), name="blog_list"),
    
    path("api/v1/users/", UserList.as_view()), # new
    path("api/v1/users/<int:pk>/", UserDetail.as_view()), 
]