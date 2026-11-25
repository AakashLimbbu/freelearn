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
    path(
    'resources/',
    views.resources,
    name='resources'
),
path(
    'admin-resources/',
    views.admin_resources,
    name='admin-resources'
),
path(
    'approve-resource/<int:resource_id>/',
    views.approve_resource,
    name='approve-resource'
),
path(
    'reject-resource/<int:resource_id>/',
    views.reject_resource,
    name='reject-resource'
),
path(
    'resource/<int:resource_id>/',
    views.resource_detail,
    name='resource-detail'
),
path(
    'edit-resource/<int:resource_id>/',
    views.edit_resource,
    name='edit-resource'
),
path(
    'delete-resource/<int:resource_id>/',
    views.delete_resource,
    name='delete-resource'
),
]

