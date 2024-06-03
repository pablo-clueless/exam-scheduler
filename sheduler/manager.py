import json
from django.db import models
from django.apps import apps
from django.core.serializers.json import DjangoJSONEncoder



class RegisteredCoursesManager(models.Manager):
        def get_exams_for_student(self, student):
            # Dynamically fetch the models
            Exam = apps.get_model('sheduler', 'Exam')
            RegisteredCourses = apps.get_model('sheduler', 'RegisteredCourses')

            # Get all the course IDs the student is registered for
            registered_courses = RegisteredCourses.objects.filter(student=student).values_list('course', flat=True)

            # Get all the exams related to those courses
            exams = Exam.objects.filter(course__in=registered_courses).select_related('course')
            
            print(registered_courses)
            
            return exams
        