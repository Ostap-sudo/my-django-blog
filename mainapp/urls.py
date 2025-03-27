from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('about/', views.about, name='about'),  # Сторінка "Про мене"
    path('contact/', views.contact, name='contact'),
    path('', views.recent_posts, name='recent_posts'),# Головна сторінка
]