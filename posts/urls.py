from django.urls import path
from .views import *
urlpatterns = [
    #path('create/', create, name='create'),
    path('search/', SearchView.as_view(), name='search'),
    #path('search/', search, name='search'),
    path('mail/', MailView.as_view(), name='mail')
    #path('mail/', mail, name='mail')
]