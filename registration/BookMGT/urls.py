from django.urls import path
from .views import *

urlpatterns = [
    path('',list_Books.as_view()),
    path('CB',Create_Books.as_view()),
    path('UB/<pk>/',Update_Books.as_view()),
    path('DB/<pk>/',Delete_Books.as_view()),
    path('RB/<pk>/',Read_Books.as_view())
]
