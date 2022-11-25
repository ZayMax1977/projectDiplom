from django.contrib import admin
from .models import Adv, Category


class AdvAdmin(admin.ModelAdmin):

    list_display = ['id','title','prise','phone_number', 'last_num_phone','trim25','district','street','town', 'building_number',
                    'name_seller','login','property_type','number_rooms', 'square_living', 'purpose_of_the_land','land_area',
                    'number_floors',
'updated_at','created_at','photo1','photo2','photo3','photo4','photo5','photo6','is_published','art','category','views']
    #
    list_display_links = ('id',"title")
    search_fields = ['id','title','phone_number']
    list_filter = ('id','phone_number','street')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(Adv,AdvAdmin)
admin.site.register(Category, CategoryAdmin)
