from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main*page'),
    path('weight_page/', views.weight_page, name='weight_page'),
    path('test_request_page/', views.test_request, name='test*request'),
    path('test_response_page/', views.test_response, name='test*response'),
    path('api_request_page/', views.api_weather_request, name='api*request'),
    path('api_response_page/', views.api_weather_response, name='api*response'),
]