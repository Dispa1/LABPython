from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL-путь для отображения списка записей в блоге
    path('', views.PostView.as_view(), name='post_list'),

    # URL-путь для отображения деталей записи в блоге с использованием параметра pk
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

    # URL-путь для добавления комментариев к записи с использованием параметра pk
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),

    # URL-путь для добавления лайка к записи с использованием параметра pk
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),

    # URL-путь для удаления лайка к записи с использованием параметра pk
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),

    
]
