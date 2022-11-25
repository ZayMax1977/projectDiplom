from django.urls import path
from .views import *

urlpatterns = [
    path('',tourism, name='tourism'),
    path('category/<int:category_id>/', get_category, name ='category'),
    path('tourism/<int:tourism_id>/', view_tourism, name='view_tourism'),
    path('add_tourism/', add_tourism, name='add_tourism'),
    path('add_tourism_ok/', add_tourism_ok, name='add_tourism_ok'),

]