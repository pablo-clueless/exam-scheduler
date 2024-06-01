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
        
        
class CustomUserManager(models.Manager):
    def get_user_details_as_json(self, user_id):
        
        CustomUser = apps.get_model('sheduler', 'CustomUser')
        try:
            user = self.get(pk=user_id)
            user_details = {
                'id': str(user.id),
                'full_name': user.full_name,
                'email': user.email,
                'role': user.role,
                'is_staff': user.is_staff,
            }
            return json.dumps(user_details, cls=DjangoJSONEncoder)
        except CustomUser.DoesNotExist:
            return json.dumps({'error': 'User not found'}, cls=DjangoJSONEncoder)