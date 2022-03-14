from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class RaceEthnicity(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class HearAboutUs(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name    

class Cohort(models.Model):
    name = models.CharField(max_length=300)
    # current = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class General(models.Model):
    current_cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, blank=True, null=True)

# https://docs.google.com/forms/d/e/1FAIpQLSdn3LASp742kqN3YhT-w6IUabl0oTW73V7W-zFIvIumB8si0w/viewform
# Students
class Student(models.Model):
    #user
    cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    discord_name = models.CharField(max_length=100, blank=True, null=True)
    twitch_name = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    sd_job = models.BooleanField(default=False)
    sd_start_salary = models.TextField(blank=True, null=True)
    why_interested = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    race_ethnicity = models.ForeignKey(RaceEthnicity, on_delete=models.SET_NULL, blank=True, null=True)
    hear_about = models.ForeignKey(HearAboutUs, on_delete=models.SET_NULL, blank=True, null=True)
    need_accomodations = models.BooleanField(default=False)
    accomodations_desc = models.TextField(blank=True, null=True)
    desc_from_student = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.email

# Assignment - Assignment name, assignment description, class #, description of link
class Assignment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    class_num = models.CharField(max_length=100) #character just in case
    link_description = models.TextField()

    def __str__(self):
        return self.name

# Assignments Turnin - student, link to code
class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=500)
    submitted_inst = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assignment} - {self.student}"