import random

from django.urls import path

from .views import *
from .views import ViewAdvDetailView


urlpatterns = [
    # path('', adv, name="adv"),
    path('category/<int:category_id>/', get_category, name='category'),
    path('sub_category/', get_subcategory, name='subcategory'),
    path('add_adv/', ViewAdvCreateView.as_view(), name='create_adv'),

    # path('add_adv/', add_adv, name='add_adv'),
    path('add_adv_ok/', add_adv_ok, name='add_adv_ok'),
    path('adv/<int:pk>/', ViewAdvDetailView.as_view(), name='view_adv'),
    path('', ViewAdvListView.as_view(), name='adv'),

    path('adv/<int:pk>/update/',AdvUpdateView.as_view(), name='update_adv'),

    # path('adv/<int:adv_id>/', view_adv, name='view_adv'),

]
