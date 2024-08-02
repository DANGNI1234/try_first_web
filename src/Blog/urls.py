from django.urls import path
from .views import index, def_mate

urlpatterns = [
    path('<str:mate>/', def_mate),
    path('', index),
]