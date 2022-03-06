from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.
def hello(request):
    return HttpResponse("HI")

def students(request):
    students = Student.objects.all()

    context = {
        "students": students
    }
    return render(request, 'students.html', context)
