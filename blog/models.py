from django.db import models
from taggit.managers import TaggableManager

# Модель для записей в блоге
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')  # Поле для изображения записи
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title}, {self.author}'  # Метод для отображения объекта

    class Meta:
        verbose_name = 'Запись'  # Название модели в единственном числе
        verbose_name_plural = 'Записи'  # Название модели во множественном числе

# Модель для комментариев к записям
class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)  # Ссылка на запись

    def __str__(self):
        return f'{self.name}, {self.post}'  # Метод для отображения объекта

    class Meta:
        verbose_name = 'Комментарий'  # Название модели в единственном числе
        verbose_name_plural = 'Комментарии'  # Название модели во множественном числе

# Модель для хранения лайков к записям
class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)  # Ссылка на запись, к которой относится лайк