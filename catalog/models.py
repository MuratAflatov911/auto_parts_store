from django.db import models
from django.urls import reverse


class VehicleMake(models.Model):
    name = models.CharField('Марка', max_length=100)

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE, related_name='models', verbose_name='Марка')
    name = models.CharField('Модель', max_length=100)

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'

    def __str__(self):
        return f'{self.make.name} {self.name}'


class VehicleGeneration(models.Model):
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='generations', verbose_name='Модель')
    name = models.CharField('Поколение', max_length=100)

    class Meta:
        verbose_name = 'Поколение автомобиля'
        verbose_name_plural = 'Поколения автомобилей'

    def __str__(self):
        return f'{self.model} {self.name}'


class VehicleEngine(models.Model):
    generation = models.ForeignKey(VehicleGeneration, on_delete=models.CASCADE, related_name='engines', verbose_name='Поколение')
    name = models.CharField('Двигатель', max_length=120)
    year_from = models.PositiveIntegerField('Год с')
    year_to = models.PositiveIntegerField('Год по', null=True, blank=True)
    volume = models.CharField('Объем', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'

    def __str__(self):
        return f'{self.generation}: {self.name}'


class Category(models.Model):
    name = models.CharField('Название', max_length=120)
    slug = models.SlugField('Slug', unique=True)
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    compatible_engines = models.ManyToManyField(VehicleEngine, blank=True, related_name='products', verbose_name='Совместимые двигатели')
    name = models.CharField('Название', max_length=220)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    old_price = models.DecimalField('Старая цена', max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField('Остаток', default=0)
    article = models.CharField('Артикул', max_length=50)
    brand = models.CharField('Бренд', max_length=80)
    image = models.ImageField('Основное изображение', upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    is_popular = models.BooleanField('Популярный товар', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField('Изображение', upload_to='products/gallery/')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f'Изображение: {self.product.name}'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=180)
    content = models.TextField('Текст новости')
    image = models.ImageField('Изображение', upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField('Название', max_length=180)
    description = models.TextField('Описание')
    percent = models.PositiveIntegerField('Процент скидки')
    active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.title} ({self.percent}%)'
