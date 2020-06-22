from django.shortcuts import render, redirect, reverse
from .choices import countries
from posts.models import Post
from posts.models import Comment
from django.contrib.auth.models import User
from django.views.generic import View, ListView, TemplateView, DetailView
# Create your views here.
class IndexListView(ListView):
    model = Post
    template_name = 'pages/index.html'
    context_object_name = 'pst'
    def get_queryset(self):
        return Post.objects.order_by('-post_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries']= countries
        context['values']= self.request.GET.get
        return context
    

    
'''
def index(request):
    post = Post.objects.order_by('-post_date')
    context = {
        'countries': countries,
        'values': request.GET,
        'pst':post
    }
    return render(request,'pages/index.html',context)
'''
class AboutView(TemplateView):
    template_name = 'pages/about.html'
'''
def about(request):
    return render(request,'pages/about.html')
'''
class ContactView(TemplateView):
    template_name = 'pages/contact.html'
'''   
def contact(request):
    return render(request,'pages/contact.html')
'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(pk=self.kwargs['pk'])
        comment = Comment.objects.order_by('-comment_date').filter(comment_post=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['pst'] = posts
        context['comment'] = comment
        return context

    def post(self, request, *args, **kwargs):
            com = request.POST.get('comment')
            user_id = request.POST.get('user_id')
            post_id = request.POST.get('post_id')
            user = User.objects.get(id=user_id)
            post = Post.objects.get(id=post_id)
            comt = Comment(comment=com, comment_user=user, comment_post=post)
            comt.save()
            return redirect(reverse("post", kwargs={
                'pk': self.kwargs['pk']
            }))
'''
def post(request,pk):
    if request.method == 'POST':
        com = request.POST['comment']
        user_id = request.POST['user_id']
        post_id = request.POST['post_id']
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        comt = Comment(comment=com, comment_user=user, comment_post=post)
        comt.save()
    posts = Post.objects.filter(pk=pk)
    comment = Comment.objects.order_by('-comment_date').filter(comment_post=pk)
    context = {
        'pst':posts,
        'comment':comment
    }
    return render(request, 'pages/post.html', context)
'''