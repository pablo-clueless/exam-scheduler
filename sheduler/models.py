import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _lazy
from django.utils import timezone

from sheduler.manager import RegisteredCoursesManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100, verbose_name=_lazy("Full Name"), null=True, blank=False)
    role = models.CharField(max_length=20, choices=(('student', 'Student'), ('supervisor', 'Supervisor'), ('exam_officer', 'Exam_Officer')), default='student')
    email = models.EmailField(max_length=255, verbose_name=_lazy("Email Address"), unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _lazy("User")
        verbose_name_plural = _lazy("Users")

    def __str__(self):
        return self.full_name or self.email
    
    

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100)

    def __str__(self):
        return self.faculty_name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    department_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default="")
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255, default="NO CODE YET")
    description = models.TextField()
    date_addedd = models.DateField(default=timezone.now)
    

    def __str__(self):
        return self.course_name


class SupervisorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supervisor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, limit_choices_to={'role': 'supervisor'}, related_name='supervisor_assignments')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=20, default='123456', null=True, blank=True)
    job_title = models.CharField(max_length=20, default='123456', null=True, blank=True)
    
    def __str__(self):
        return str(self.supervisor)


class ExamOfficerProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam_officer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, limit_choices_to={'role': 'exam_officer'}, related_name='exam_officer_assignments')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=20, default='123456', null=True, blank=True)
    job_title = models.CharField(max_length=20, default='123456', null=True, blank=True)

    def __str__(self):
        return str(self.exam_officer)


class StudentProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_reg_number = models.CharField(max_length=15)
    student = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, related_name='studentprofile')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    matriculated = models.BooleanField(default=False)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.student)


class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, )
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    supervisors = models.ManyToManyField(SupervisorProfile, related_name='exams_supervised')
    exam_officer = models.ForeignKey(ExamOfficerProfile, on_delete=models.DO_NOTHING, related_name='exams_assigned')
    teken = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course} Exam at {self.venue} on {self.date_time}'


class ExamAttendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, related_name='attendances')
    attended = models.BooleanField(default=False)


class RegisteredCourses(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
   
    
    objects = RegisteredCoursesManager()
    def __str__(self):
        return str(self.student)
    
    
class ExamMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField("exam/material", blank=True, null=True)

    def __str__(self):
        return self.title

class ExamReevaluationRequest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('reviewed', 'Reviewed')), default='pending')

    def __str__(self):
        return f'Reevaluation Request by {self.student}'