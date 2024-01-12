from django.contrib import admin
from .models import Category, Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fileds = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'author', 'status')
    list_editable = ('is_featured',)
    
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)


