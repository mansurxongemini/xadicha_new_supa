from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarjimai-hol/', views.biography_view, name='biography'),
    path('ilmiy-meros/', views.books_view, name='books'),
    path('maqolalar/', views.articles_view, name='articles'),
    path('videolar/', views.videos_view, name='videos'),
    path('loyiha-haqida/', views.about_view, name='about'),
    path('bloglar/', views.blog_list_view, name='blog_list'),
    path('bloglar/<int:pk>/', views.blog_detail_view, name='blog_detail'),
]
