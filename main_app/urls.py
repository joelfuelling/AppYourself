from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('roles/', views.RoleList.as_view(), name='index'),
    path('roles/create', views.RoleCreate.as_view(), name='roles_create'),
    path('roles/<int:pk>', views.RoleDetail.as_view(), name='role_detail'),
    path('roles/<int:pk>/update', views.RoleUpdate.as_view(), name='roles_update'),
    path('roles/<int:pk>/delete', views.RoleDelete.as_view(), name='roles_delete'),
    path('roles/<int:pk>/add_followup', views.add_followup, name='add_followup'),
    #! pk will not be desireable with M:M
    path('roles/<int:role_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('roles/<int:role_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
    path('tags/', views.TagList.as_view(), name='tag_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
]