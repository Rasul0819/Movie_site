from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 100,unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('movies:category',args=[self.slug])

    
class Movies(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название фильма')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    realised_date = models.DateField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание фильма')
    image = models.ImageField(verbose_name='Обложка фильма',upload_to='images')
    trailer = models.URLField(verbose_name = 'Ссылка для трейлера',blank=True,null=True)

    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('movies:movie',args=[self.id,self.slug,])
    

    
class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.author} к {self.movie}'


