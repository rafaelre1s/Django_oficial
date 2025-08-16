from django.contrib import admin

# Register your models here.
from core.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}