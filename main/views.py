from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student, Assignment, Cohort, Gender, RaceEthnicity, HearAboutUs
from .forms import StudentForm, AssignmentForm

# Create your views here.
def admin(request):
    cohorts = Cohort.objects.all()
    genders = Gender.objects.all()
    race_ethnicity = RaceEthnicity.objects.all()
    hear_about_us = HearAboutUs.objects.all()

    context = {
        "cohorts": cohorts,
        "genders": genders,
        "race_ethnicity": race_ethnicity,
        "hear_about_us": hear_about_us
    }
    return render(request, 'admin.html', context)

def hello(request):
    return HttpResponse("HI")

def students(request):
    students = Student.objects.all()

    context = {
        "students": students
    }
    return render(request, 'students.html', context)

def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students') 

    context = {
        "student": student,
        "form": form
    }
    return render(request, 'student_edit.html', context)

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('students') 

    form = StudentForm()
    context = {
        "form": form
    }
    return render(request, 'student_create.html', context)

def assignments(request):
    assignments = Assignment.objects.all()

    context = {
        "assignments": assignments
    }
    return render(request, 'assignments.html', context)

def assignment_edit(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    form = AssignmentForm(instance=assignment)

    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments')

    context = {
        "assignment": assignment,
        "form": form
    }
    return render(request, 'assignment_edit.html', context)

def assignment_create(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('assignments') 

    form = AssignmentForm()
    context = {
        "form": form
    }
    return render(request, 'assignment_create.html', context)