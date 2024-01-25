from django.urls import path, include
from adminview import  views

urlpatterns = [
    path('', views.admin_birds_status, name='admin_birds_status'),
    path('admin_add_birds_status', views.admin_add_birds_status, name='admin_add_birds_status'),
    path('admin_birds_detail', views.admin_birds_detail, name='admin_birds_detail'),
    path('admin_add_birds_detail', views.admin_add_birds_detail, name='admin_add_birds_detail'),
    
]