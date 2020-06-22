from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    #path('dashboard/', views.dashboard, name='dashboard'), 
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'), 
    #path('register/', views.register, name='register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('login/', views.login, name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    #path('logout/', views.logout, name='logout'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('delete/', views.delete_post, name='delete_post'),
    path('delete/', views.PostDeleteView.as_view(), name='delete_post'),
    #path('update/<int:id>/', views.update_post, name='update_post')
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update_post')
    ]