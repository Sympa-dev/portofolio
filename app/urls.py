from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('robots.txt', robots_txt),
]