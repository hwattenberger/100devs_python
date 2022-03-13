from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

from .models import Student, Assignment, Cohort, Gender, RaceEthnicity, HearAboutUs, StudentAssignment
from .forms import StudentForm, AssignmentForm, AssignmentTurninForm

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

def admin_cohort(request):
    if request.method == "POST":
        name=request.POST.get('value')
        if name:
            Cohort.objects.create(
                name=name
            )
        else:
            return HttpResponse("Not a valid name")

    return redirect('admin')

def admin_cohort_edit(request, id):
    data_from_post = json.load(request)['value']
    cohort = Cohort.objects.get(id=id)
    cohort.name = data_from_post
    cohort.save(update_fields=['name'])
    return HttpResponse("success")

def admin_race_eth(request):
    if request.method == "POST":
        name=request.POST.get('name')
        if name:
            RaceEthnicity.objects.create(
                name=name
            )
        else:
            return HttpResponse("Not a valid name")

    return redirect('admin')

def admin_race_eth_edit(request, id):
    data_from_post = json.load(request)['value']
    re = RaceEthnicity.objects.get(id=id)
    re.name = data_from_post
    re.save(update_fields=['name'])
    return HttpResponse("success")

def admin_gender(request):
    if request.method == "POST":
        name=request.POST.get('name')
        if name:
            Gender.objects.create(
                name=name
            )
        else:
            return HttpResponse("Not a valid name")

    return redirect('admin') 

def admin_gender_edit(request, id):
    data_from_post = json.load(request)['value']
    gender = Gender.objects.get(id=id)
    gender.name = data_from_post
    gender.save(update_fields=['name'])
    return HttpResponse("success")

def admin_heard(request):
    if request.method == "POST":
        name=request.POST.get('name')
        if name:
            HearAboutUs.objects.create(
                name=name
            )
        else:
            return HttpResponse("Not a valid name")

    return redirect('admin')

def admin_heard_edit(request, id):
    data_from_post = json.load(request)['value']
    heard = HearAboutUs.objects.get(id=id)
    heard.name = data_from_post
    heard.save(update_fields=['name'])
    return HttpResponse("success")

def submit_assignment(request):
    if request.method == "POST":
        email=request.POST.get('email')
        assignment=request.POST.get('assignment')
        link=request.POST.get('assignment')

        try:
            this_student=Student.objects.get(email=email)
            this_assign=Assignment.objects.get(id=assignment)
        except:
            return HttpResponse("Not a valid student")

        StudentAssignment.objects.create(
            student=this_student,
            assignment=this_assign,
            link=link
        )
        return redirect('admin') 
    
    form = AssignmentTurninForm()
    # assignments = Assignment.objects.all()
    context = {
        "form": form
        # "assignments": assignments
    }
    return render(request, 'assignment-turnin.html', context)