from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.book_detail, name='book_detail'),
]
