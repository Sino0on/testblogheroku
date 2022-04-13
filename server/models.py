from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='Тут пусто')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created']
