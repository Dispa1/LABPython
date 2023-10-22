"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Импортируем модуль административной панели Django
from django.contrib import admin

# Импортируем функции для работы с URL
from django.urls import path, include

# Импортируем модуль настроек Django
from django.conf import settings

# Импортируем функцию для обслуживания медиа-файлов в режиме отладки
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap


sitemaps = {
 'posts': PostSitemap,
}

# Определяем список URL-путей
urlpatterns = [
    # URL для административной панели Django
    path('admin/', admin.site.urls),

    # Включаем URL-паттерны из приложения 'blog'
    path('', include('blog.urls')),

    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]

# Проверяем, находится ли приложение в режиме отладки
if settings.DEBUG:
    # Если да, то добавляем URL-путь для обслуживания медиа-файлов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

