from django import forms
from .models import Comments

# Создаем форму для комментариев на основе модели Comments
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments  # Указываем модель, на основе которой создается форма
        fields = ('name', 'email', 'text_comments')  # Указываем поля, которые будут отображаться в форме
