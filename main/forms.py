# from django.forms import ModelForm
from django import forms
from .models import Student, Assignment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = []

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        labels = {
            "name": "Assignment name",
            "class_num": "Class number",
            "link_description": "Description associated with link"
        }
        exclude = []

class AssignmentTurninForm(forms.Form):
    assignments = Assignment.objects.all()
    # assignments = list(Assignment.objects.all())
    assign_list = []

    for assignment in assignments:
        assign_list.append((assignment.id, assignment.name))

    email = forms.CharField(label='Your email address')
    assignment = forms.CharField(label='What assignment?', widget=forms.Select(choices=assign_list))
    link = forms.CharField(label="Your link")