from django.contrib import admin

# Register your models here.
from .models import Tourism, Category


class TourismAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','author','source','trim25','is_published')
    list_display_links = ('id',"title")
    search_fields = ('title','content')

    list_editable = ("is_published",)
    list_filter = ("is_published", "category")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(Tourism,TourismAdmin)
admin.site.register(Category, CategoryAdmin)