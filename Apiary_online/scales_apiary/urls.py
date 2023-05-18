from django.urls import path
from . import views
from .views import line_chart, line_chart_json

urlpatterns = [
    path('', views.main_page, name='main*page'),
    path('weight_page/', views.weight_page, name='weight_page'),
    path('test_request_page/', views.test_request, name='test*request'),
    path('test_response_page/', views.test_response, name='test*response'),
    path('api_request_page/', views.api_weather_request, name='api*request'),
    path('api_response_page/', views.api_weather_response, name='api*response'),
    # path('weight_page/test_chart', views.chart_1, name='test*chart*1'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('chart_humidity', views.line_chart_humidity, name='line*chart*humidity'),
]