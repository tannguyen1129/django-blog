from rest_framework import serializers
from .models import Blog

from django.contrib.auth import get_user_model 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')
        model = Blog
        
class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)