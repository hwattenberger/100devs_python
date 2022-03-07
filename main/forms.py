from django.forms import ModelForm
from .models import Student, Assignment

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = []

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        labels = {
            "name": "Assignment name",
            "class_num": "Class number",
            "link_description": "Description associated with link"
        }
        exclude = []