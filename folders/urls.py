from django.urls import path
from . import views

urlpatterns = [
    path('', views.folder_list, name='folder_list'),
    path('<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('<int:folder_id>/children/', views.folder_children, name='folder_children'),
]
