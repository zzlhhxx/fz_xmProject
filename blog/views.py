from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def blog_detail(request,blog_id):
    return render(request,'blog_detail.html')