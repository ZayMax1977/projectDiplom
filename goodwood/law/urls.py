from django.urls import path

from .views import *

urlpatterns = [
    path('', law, name = "law"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('law/<int:law_id>/', view_law, name='view_law'),
    path('add_law/', add_law, name='add_law'),
    path('add_law_ok/', add_law_ok, name='add_law_ok'),

]