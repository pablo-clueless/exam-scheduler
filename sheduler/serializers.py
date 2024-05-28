from django.db import IntegrityError
from rest_framework import serializers
from .models import Course, CustomUser, Department, ExamAttendance, ExamMaterial, ExamOfficerProfile, Exam, ExamReevaluationRequest, Faculty, RegisteredCourses, StudentProfile, SupervisorProfile
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = CustomUser
        feild = "__all__"
        
class CreateUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    role = serializers.ChoiceField(choices=(('student', 'Student'), ('supervisor', 'Supervisor'), ('exam_officer', 'Exam Officer')), required=True)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True, 'unique': True},
        }

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        role = validated_data.pop('role', 'student')

        validated_data['username'] = email

        user = CustomUser.objects.create_user(
            full_name=full_name, email=email, password=password, role=role, **validated_data
        )
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')

            return user
        else:
            raise serializers.ValidationError('Must include "email" and "password".')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name', 'faculty']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'department', 'description']

    def validate_course_name(self, value):
        if Course.objects.filter(course_name=value).exists():
            raise serializers.ValidationError("A course with this name already exists.")
        return value
    
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'course', 'date_time', 'venue', 'supervisors', 'exam_officer']


class SupervisorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorProfile
        fields = ['id', 'supervisor',  'department', 'employee_id', 'job_title']


class ExamOfficerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamOfficerProfile
        fields = ['id', 'exam_officer','department', 'employee_id', 'job_title']


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'student_reg_number', 'student', 'department', 'matriculated', 'year']
        
        
class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExamAttendance
        fields = "__all__"

    def validate(self, data):
        exam = data.get('exam')
        student = data.get('student')
        
        if ExamAttendance.objects.filter(exam=exam, student=student).exists():
            raise serializers.ValidationError("This student has been marked attended")
        
        return data
    

    
class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCourses
        fields = ['id', 'student', 'course']

    def validate(self, data):
        student = data.get('student')
        course = data.get('course')
        
        if RegisteredCourses.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("You have registered for this course.")
        
        return data
    
    
class RegisteredCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCourses
        fields = ['id', 'student', 'course']
        
        
class ExamMaterialSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=True)
    title = serializers.CharField(required=True)
    file = serializers.FileField(required=True)

    class Meta:
        model = ExamMaterial
        fields = ['id', 'course', 'title', 'description', 'file']

class ExamReevaluationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamReevaluationRequest
        fields = ['id', 'student', 'exam', 'request_date', 'feedback', 'status']
        
class ExamMarkTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'taken']