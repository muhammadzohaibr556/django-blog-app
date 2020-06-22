from django.urls import path
from . import views
urlpatterns = [
    #path('', views.index, name='index'), 
    path('', views.IndexListView.as_view(), name='index'), 
    #path('about/', views.about, name='about'),
    path('about/', views.AboutView.as_view(), name='about'),
    #path('contact/', views.contact, name='contact'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    #path('post/<int:pk>/', views.post, name='post')
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post')
]
