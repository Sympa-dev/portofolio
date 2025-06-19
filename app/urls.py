from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('download_cv/', download_cv, name='download_cv'),
    path('sendmail/', SendMail, name="sendmail"),
    path('robots.txt', robots_txt),
]