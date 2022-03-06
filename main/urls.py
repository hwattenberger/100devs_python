from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('students/', views.students)
]