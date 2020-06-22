from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, Comment
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import View
from django.core.mail import send_mail
# Create your views here.

'''def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
        id = request.POST['id']
        user = User.objects.get(id=id)
        if 'photo' in request.FILES:
            post = Post(title=title, description=description, photo=photo, post_user=user )
        else:
            post = Post(title=title, description=description, post_user=user )
        post.save()
        messages.success(request, 'You have successfully made a new post...')
        return redirect('dashboard')
'''
class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset_list = Post.objects.all()
        # Keywords
        if request.GET.get('keywords'):
            keywords = request.GET.get('keywords')
            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)
        
        if request.GET.get('title'):
            title = request.GET.get('title')
            if title:
                queryset_list = queryset_list.filter(title__icontains=title)
        context = {
            'pst':queryset_list,
            'values': request.GET.get
        }      
        return render(request,'pages/index.html', context)

'''
def search(request):
    queryset_list = Post.objects.all()
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)

    context = {
        'pst':queryset_list,
        'values': request.GET
    }      
    return render(request,'pages/index.html', context)
'''
class MailView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('your_message')
        send_mail(
            'Information Technology Blog',
            'Hi '+name+', We have recieved your message, it is stated that we will come back to you as soon as possible. ThankYou for your message ',
            'muhammadzohaibr556@gmail.com',
            [email],
            fail_silently=False
        )
        return render(request,'pages/contact.html')        
'''
def mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['your_message']
    send_mail(
        'Information Technology Blog',
        'Hi '+name+', We have recieved your message, it is stated that we will come back to you as soon as possible. ThankYou for your message ',
        'muhammadzohaibr556@gmail.com',
        [email],
        fail_silently=False
    )
    return render(request,'pages/contact.html')
'''