from django.shortcuts import render,redirect
from home.models import Contact
from blog.models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,login
from .forms import AddForm
#from .forms import AddForm


# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        content=request.POST['content']
        contact=Contact(name=name,email=email,contact=contact,content=content)
        contact.save()
        return redirect('home')
    #else:
       # return HttpResponse('page not found')
    return render(request,'home/contact.html')        
 

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        user.save()
        return redirect('/')

    else:
        return HttpResponse("signup failed")

       

def login_view(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            auth.login(user,request)
            return redirect('/')
           

    else:
            return HttpResponse("Error Occured")

def logout_view(request):
    logout(request)
    return redirect('/')

def addpost(request):
    if request.method=='POST':
        form=AddForm(request.POST,request.FILES)
        if form.is_valid():
            form_item=form.save(commit=False)
            form_item.save()
            return redirect('/')
    else:
        form=AddForm()
   
    return render(request,'home/addpost.html',{'form':form})


def search_view(request):
    query=request.GET['xyz']
    if len(query)>100:
        post=Post.objects.none()
    else:
        postTitle=Post.objects.filter(title__icontains=query)
        postContent=Post.objects.filter(content__icontains=query)
        post=postTitle.union(postContent)

    params={'post':post,'query':query}
    return render(request,'home/search.html',params)



