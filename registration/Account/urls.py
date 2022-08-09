from django.urls import path
from .views import *

urlpatterns = [
    path('',List_User.as_view()),
    path('CU',Create_User.as_view()),
    path('RU/<pk>/',Read_User.as_view()),
    path('UU/<pk>/',Update_User.as_view()),
    path('DU/<pk>/',Delete_User.as_view())
]
