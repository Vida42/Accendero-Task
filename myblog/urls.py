from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('about', views.about, name='about'),
]
