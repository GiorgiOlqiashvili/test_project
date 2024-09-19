from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.reader_form, name='reader_form'),
]
