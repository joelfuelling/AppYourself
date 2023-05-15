from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('roles/', views.RoleList.as_view(), name='index'),
    path('roles/create', views.RoleCreate.as_view(), name='roles_create'),
    path('roles/<int:pk>', views.roles_detail, name='role_detail'),
]