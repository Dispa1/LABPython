from django.apps import AppConfig

# Определяем конфигурацию приложения 'blog'
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Устанавливаем тип автоматического поля для создания первичных ключей
    name = 'blog'  # Указываем имя приложения
