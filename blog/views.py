from django.shortcuts import render
from .models import Post

# Create your views here.
def blogHome(request):
    post=Post.objects.all()
    return render(request,'blog/blogHome.html',{'post':post})

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    return render(request,'blog/blogPost.html',{'post':post})

