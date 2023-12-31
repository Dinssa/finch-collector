from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('finches/', views.finch_index, name='finch_index'),
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finch/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]