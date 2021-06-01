from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book-search/', views.book_search, name='book_search')
]