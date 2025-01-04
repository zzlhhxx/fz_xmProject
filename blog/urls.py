from django.urls import path
from . import views

name_app='blog'
urlpatterns = [
    path('',views.index,name="index")
]