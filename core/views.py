from telnetlib import STATUS
from django.shortcuts import render
from blog.models import Post

 

def frontPage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontPage.html', {'posts':posts})

def about(request):
    return render(request, 'core/about.html')