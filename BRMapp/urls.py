from django.contrib import admin
from django.urls import path
from BRMapp import views

urlpatterns = [
    path('newbook/',views.newBook),
    path('add',views.add),
    path('view-books',views.viewBooks),
]
