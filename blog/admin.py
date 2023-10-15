from django.contrib import admin    
from .models import Post, Comments, Likes

# Регистрируем модель Post в административной панели Django
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Определяем, какие поля отображать в списке записей

# Регистрируем модель Comments в административной панели Django
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')  # Определяем, какие поля отображать в списке комментариев

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('ip', 'post')
