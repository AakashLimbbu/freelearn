from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
    path(
    'my-resources/',
    views.my_resources,
    name='my-resources'
),
    path(
    'upload-resource/',
    views.upload_resource,
    name='upload-resource'
),

]

