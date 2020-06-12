from django.shortcuts import render
from .models import Job
from blog.models import Blog

# Create your views here.


def home(request):
    
    last = Blog.objects.latest('pub_date')
    blogs = Blog.objects.all().order_by('-id')[1:5]
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'blogs':blogs, 'last':last})