from django.shortcuts import render, redirect, reverse
from .models import UserInfo
from django.contrib import messages, auth
from django.contrib.auth.models import User
from posts.forms import PostForm
from posts.models import Post
from django.views.generic import View, ListView, UpdateView
from django.urls import reverse_lazy
#from .forms import RegisterForm
# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'pages/index.html')        

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        c_password = request.POST.get('cpwd')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('index')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('index')
                else:
                    reg = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    reg.save()
                    reginfo = UserInfo(gender=gender, country=country, info=reg)
                    reginfo.save()
                    messages.success(request, 'You are now register and you can log in')
                    return redirect('index')
        else:
            messages.error(request,'Password do not match')
            return redirect('index')
'''
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['pwd']
        c_password = request.POST['cpwd']
        gender = request.POST['gender']
        country = request.POST['country']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('index')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('index')
                else:
                    reg = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    reg.save()
                    reginfo = UserInfo(gender=gender, country=country, info=reg)
                    reginfo.save()
                    messages.success(request, 'You are now register and you can log in')
                    return redirect('index')
        else:
            messages.error(request,'Password do not match')
            return redirect('index')

    else:
        return render(request,'pages/index.html')
'''
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'pages/index.html')
    def post(self, request, *args, **kwargs):
        username = request.POST.get('userl')
        password = request.POST.get('pwdl')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logg in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')

'''
def login(request):
    if request.method == 'POST':
        username = request.POST['userl']
        password = request.POST['pwdl']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logg in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('index')

    else:
        return render(request,'pages/index.html')
'''
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
'''
def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
'''

class DashboardView(ListView):
    form = PostForm()
    model = Post
    template_name = 'accounts/dashboard.html'
    context_object_name = 'pst'
    def get_queryset(self):
        return Post.objects.order_by('-post_date').filter(post_user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = UserInfo.objects.get(info=self.request.user.id)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            if 'photo' in request.FILES:
                photo = request.FILES.get('photo')
            id = request.POST.get('id')
            user = User.objects.get(id=id)
            if 'photo' in request.FILES:
                blogpost = Post(title=title, description=description, photo=photo, post_user=user )
            else:
                blogpost = Post(title=title, description=description, post_user=user )
            blogpost.save()
            messages.success(request, 'You have successfully made a new post...')
        return redirect('dashboard')

#from django.contrib.auth.decorators import login_required
#@login_required
'''def dashboard(request):
    form= PostForm(request.POST or None)
    post = Post.objects.order_by('-post_date').filter(post_user=request.user.id)
    user_info = UserInfo.objects.get(info=request.user.id)
    context = {
        'form':form,
        'info':user_info,
        'pst':post
    }
    return render(request, 'accounts/dashboard.html', context)
'''
class PostDeleteView(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('input_id')
        pst = Post.objects.get(id=id)
        pst.delete()
        return redirect('dashboard')
'''
def delete_post(request):
    if request.method=='POST':
        id = request.POST['input_id']
        pst = Post.objects.get(id=id)
        pst.delete()
    return redirect('dashboard')
'''
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'accounts/edit_post.html'
    context_object_name = 'post'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        form_class = PostForm(self.request.POST or None, instance=Post.objects.get(id=self.object.pk))
        context = super().get_context_data(**kwargs)
        context['form'] = form_class
        return context

    def form_valid(self, form):
        if self.request.POST['deleteImg']=="No":
            form.save()
        elif self.request.POST['deleteImg']=="Yes":
            form.save()
            Post.objects.get(pk=self.object.pk).photo.delete(save=True)

        return redirect('dashboard')
'''
def update_post(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'accounts/edit_post.html', context)
'''