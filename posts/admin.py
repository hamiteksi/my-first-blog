from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'crt_date', 'author']
    list_filter = ['crt_date']
    search_fields = ['title', 'content']
    class Meta:
        model = Post



admin.site.register(Post, PostAdmin)