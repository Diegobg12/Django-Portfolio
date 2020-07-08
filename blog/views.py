from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.

from django.shortcuts import render

def allblogs(request):
    blogs = Blog.objects
    last = Blog.objects.latest('pub_date')
    return render(request, 'allblogs.html', {'blogs': blogs, 'last':last})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': detailblog})
 
