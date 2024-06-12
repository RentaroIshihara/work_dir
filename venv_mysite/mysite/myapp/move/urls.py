# urls.py
from django.urls import path
from .views import my_view

urlpatterns = [
    path('form/', my_view, name='my-form'),
]