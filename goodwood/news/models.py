from django.db import models
# from django.urls import reverse
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Наименование")
    source = models.CharField(max_length=150, verbose_name = "Источник")
    content = models.TextField(blank=False, verbose_name = "Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата публикации")
    photo = models.ImageField(upload_to='photo_news/%Y/%m/%d',blank=True, verbose_name = "Фото")
    is_published = models.BooleanField(default = False, verbose_name = "Опубликовано")
    category = models.ForeignKey("Category", on_delete = models.PROTECT, null = True, verbose_name="Категория")
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def trim25(self):
        return u"%s..." % (self.content[:25],)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at','title' ]

class Category(models.Model):
    title = models.CharField (max_length=150,db_index=True, verbose_name  = "Наименование категории")

    # def get_absolute_url(self):
    #     return reverse('category',kwargs={'category_id': self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

