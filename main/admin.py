from django.contrib import admin
from .models import Gender, RaceEthnicity, HearAboutUs, Cohort, Student, StudentAssignment, General, Assignment

# Register your models here.
admin.site.register(Gender)
admin.site.register(RaceEthnicity)
admin.site.register(HearAboutUs)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(StudentAssignment)
admin.site.register(General)