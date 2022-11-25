from django.contrib import admin
from .models import Chance

class ChanceAdmin(admin.ModelAdmin):
    list_display = ("id", "number_phone",'created_at')
    list_display_links = ("id", "number_phone")
    search_fields = ("number_phone",)

admin.site.register(Chance,ChanceAdmin)
