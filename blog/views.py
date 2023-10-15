from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .forms import CommentsForm  # Импортируем форму для комментариев
from django.db.models import Count
from taggit.models import Tag  # Импортируйте модель Tag из django-taggit

# Представление для отображения списка записей в блоге
class PostView(View):
    def get(self, request):
        all_tags = Tag.objects.all()
        posts = Post.objects.all()
        comment_sorted_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:5]  # Выберите 3 поста с наибольшим количеством комментариев
        recent_posts = Post.objects.order_by('-date')[:3]
        return render(request, 'blog/index.html', {'post_list': posts, 'all_tags': all_tags, 'comment_sorted_posts': comment_sorted_posts, 'recent_posts': recent_posts})

# Представление для отображения деталей записи в блоге
class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        similar_posts = Post.objects.filter(tags__in=post.tags.all()).exclude(id=pk).distinct()[:5]
        return render(request, 'blog/blog_detail.html', {'post': post, 'similar_posts': similar_posts})

# Представление для добавления комментариев к записи
class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

# Функция для получения IP-адреса клиента
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Представление для добавления лайка к записи
class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

# Представление для удаления лайка к записи
class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client, post_id=pk)
            lik.delete()
        except Likes.DoesNotExist:
            return redirect(f'/{pk}')
        return redirect(f'/{pk}')
