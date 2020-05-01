from django.contrib import admin
from .models import Article
from django.contrib.auth.admin import UserAdmin
from django.conf import settings



# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'img_path',)

admin.site.register(Article, ArticleAdmin)
