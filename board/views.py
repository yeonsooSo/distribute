from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
# Create your views here.


def home(req):
    blog_objects = Blog.objects.all()
    return render(req, 'home.html', {'data': blog_objects})


def post_create(req):
    if req.method == 'POST':
        blog_object = Blog()
        blog_object.title = req.POST['title']
        blog_object.body = req.POST['body']
        blog_object.save()
        return redirect('/blog/'+str(blog_object.id))
    return render(req, 'post_create.html')


def post_read(req, id):
    blog_object = get_object_or_404(Blog, pk=id)
    return render(req, 'post_read.html', {'data': blog_object})

