from django.urls import path
from .views import *

urlpatterns = [
    path('', chance, name = 'chance'),
    path('do_chance/', do_chance, name="do_chance")
]
