from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('about', views.about, name='about'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('tags/<int:tag_pk>/', views.tag, name='tag'),
]
