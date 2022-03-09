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
    path('100devs/admin/create-cohort', views.admin_cohort, name="admin-cohort-create"),
    path('100devs/admin/create-gender', views.admin_gender, name="admin-gender-create"),
    path('100devs/admin/create-race', views.admin_race_eth, name="admin-race-create"),
    path('100devs/admin/create-heard', views.admin_heard, name="admin-heard-create"),
]