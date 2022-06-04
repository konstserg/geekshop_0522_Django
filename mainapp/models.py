from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'#{self.pk}, {self.name}'  # self--работа с текущим объектом, pk--первичный ключ


# Meta--набор настроек, относящихся к модели в целом
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')  # внешняя ссылка(внешн.ключ) на pk другой модели
    name = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')
    # blank--позволяет на сайте не заполнять какие-либо данные, null--позволяет записывать в базу пустое значение
    short_decs = models.CharField(max_length=128, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')  # decimal_places=2знаки после запятой
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.name}, {self.category.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'













