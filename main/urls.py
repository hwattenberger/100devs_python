from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('students/', views.students, name="students"),
    path('students/create/', views.student_create, name="student-create"),
    path('students/edit/<str:student_id>/', views.student_edit, name="student-edit"),
    path('assignments/', views.assignments, name="assignments"),
    path('assignments/create/', views.assignment_create, name="assignment-create"),
    path('assignments/edit/<str:assignment_id>/', views.assignment_edit, name="assignment-edit"),
    path('100devs/admin/', views.admin, name="admin"),
]