from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('weight_page/', views.weight_page, name='weight_page'),
]