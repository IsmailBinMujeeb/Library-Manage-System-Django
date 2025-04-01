from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('book/<int:book_id>/', views.book_page, name='book_page'),
    path('book/create/', views.create_book_page, name='create_book_page'),
]