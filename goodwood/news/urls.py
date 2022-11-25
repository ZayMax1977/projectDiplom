from django.urls import path

from .views import *


urlpatterns = [
    path('', news, name = 'news'),
    # path(r'^page/(\d+)/$',news),
    path('category/<int:category_id>/', get_category, name ='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('add_news/', add_news, name='add_news'),
    path('add_news_ok/', add_news_ok, name='add_news_ok'),
]
