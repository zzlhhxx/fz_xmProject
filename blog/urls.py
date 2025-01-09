from django.urls import path
from . import views

name_app='blog'
urlpatterns = [
    path('',views.index,name="index"),
    path('blog/<blog_id>',views.blog_detail,name="blog_detail"),

    path('pub_blog/pub',views.pub_blog,name='pub_blog')
]