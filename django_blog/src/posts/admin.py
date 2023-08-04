from django.contrib import admin
from posts.models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'created_on', 'last_updated')
    list_editable = ("published_on",)

admin.site.register(BlogPost, BlogPostAdmin)