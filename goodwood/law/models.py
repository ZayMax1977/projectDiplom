from django.db import models

# Create your models here.
class Law(models.Model):
    title = models.CharField(max_length=150,verbose_name = 'Наименование')
    category = models.ForeignKey("Category", on_delete= 	models.PROTECT, null = True, verbose_name="Категория")
    source = models.CharField(max_length=150,verbose_name = 'Ресурс автора', default='')
    content = models.TextField(verbose_name = 'Контент')
    author = models.CharField(max_length=100, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликоывано')


    def __str__(self):
        return self.title

    def trim25(self):
        return u"%s..." % (self.content[:25],)

    class Meta:
        verbose_name = "Право"
        verbose_name_plural = "Право"
        ordering = ['-created_at','title' ]

class Category(models.Model):
    title = models.CharField (max_length=150,db_index=True, verbose_name  = "Наименование категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
