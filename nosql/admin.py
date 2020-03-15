from django.contrib import admin
from djongo.admin import admin
from .models import *
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'views')

admin.site.register(BlogPost, BlogPostAdmin)