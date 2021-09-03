from django.urls import path
from .views import *


urlpatterns = [
    path('', ever, name='ever'),
    path('com/', com, name='com'),
]