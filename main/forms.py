# from django.forms import ModelForm
from django import forms
from .models import Student, Assignment, General

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
    current_cohort = General.objects.get(id=1).current_cohort
    assignments = list(Assignment.objects.filter(cohort=current_cohort))
    assign_list = []

    for assignment in assignments:
        assign_list.append((assignment.id, assignment.name))

    email = forms.CharField(label='Your email address')
    assignment = forms.CharField(label='What assignment?', widget=forms.Select(choices=assign_list))
    link = forms.CharField(label="Your link")

class SingleAssignmentTurninForm(forms.Form):
    email = forms.CharField(label='Your email address')
    link = forms.CharField(label="Your link")