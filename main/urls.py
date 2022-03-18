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
    path('100devs/admin/current-cohort/', views.admin_current_cohort, name="admin-current-cohort"),
    path('100devs/admin/create-cohort/', views.admin_cohort, name="admin-cohort-create"),
    path('100devs/admin/create-gender/', views.admin_gender, name="admin-gender-create"),
    path('100devs/admin/create-race/', views.admin_race_eth, name="admin-race-create"),
    path('100devs/admin/create-heard/', views.admin_heard, name="admin-heard-create"),
    path('100devs/admin/cohort/<str:id>/', views.admin_cohort_edit, name="admin-cohort-edit"),
    path('100devs/admin/gender/<str:id>/', views.admin_gender_edit, name="admin-gender-edit"),
    path('100devs/admin/re/<str:id>/', views.admin_race_eth_edit, name="admin-race-edit"),
    path('100devs/admin/heard/<str:id>/', views.admin_heard_edit, name="admin-heard-edit"),
    path('submit_assignment/', views.submit_assignment, name="submit-assignment"),
    path('submit_assignment/<str:assign_id>/', views.submit_specific_assignment, name="submit-assignment-single"),
]