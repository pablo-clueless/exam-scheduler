from django.db import IntegrityError
from rest_framework import serializers
from .models import Course, CustomUser, Department, ExamAttendance, ExamMaterial, ExamOfficerProfile, Exam, ExamReevaluationRequest, Faculty, RegisteredCourses, StudentProfile, SupervisorProfile
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'role', 'email', 'created_at', 'updated_at', 'is_staff', 'is_superuser']
     
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

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(username=email, password=password)
        
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty_name']

class DepartmentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    class Meta:
        model = Department
        fields = ['id', 'department_name', 'faculty']

class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name', 'faculty']


class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer
    
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code', 'department', 'description']

class CourseCreateSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(max_length=255)
    course_code = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code', 'department', 'description']
    
    def validate_course_name(self, value):
        if Course.objects.filter(course_name=value).exists():
            raise serializers.ValidationError("A course with this name already exists.")
        return value



class SupervisorProfileSerializer(serializers.ModelSerializer):
    supervisor = UserSerializer()  # Nesting CustomUserSerializer

    class Meta:
        model = SupervisorProfile
        fields = ['id', 'supervisor', 'department', 'employee_id', 'job_title']


class ExamOfficerProfileSerializer(serializers.ModelSerializer):
    exam_officer = UserSerializer()  # Nesting CustomUserSerializer

    class Meta:
        model = ExamOfficerProfile
        fields = ['id', 'exam_officer', 'department', 'employee_id', 'job_title']


class StudentProfileSerializer(serializers.ModelSerializer):
    student = UserSerializer()  # Nesting CustomUserSerializer

    class Meta:
        model = StudentProfile
        fields = ['id', 'student_reg_number', 'student', 'department', 'matriculated', 'year']

    

class ExamSerializer(serializers.ModelSerializer):
    supervisors = SupervisorProfileSerializer(many=True)  # Set many=True for Many-to-Many relationship
    exam_officer = ExamOfficerProfileSerializer()

    class Meta:
        model = Exam
        fields = ['id', 'course', 'date_time', 'venue', 'supervisors', 'exam_officer', 'teken']
    
class CourseRegistrationSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer()
    course = CourseSerializer()
    class Meta:
        model = RegisteredCourses
        fields = ['id', 'student', 'course']

    def validate(self, data):
        student = data.get('student')
        course = data.get('course')
        
        if RegisteredCourses.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("You have registered for this course.")
        
        return data
    
class AttendanceSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    student = StudentProfileSerializer()
    class Meta:
        model = ExamAttendance
        fields = "__all__"

    def validate(self, data):
        exam = data.get('exam')
        student = data.get('student')
        
        if ExamAttendance.objects.filter(exam=exam, student=student).exists():
            raise serializers.ValidationError("This student has been marked attended")
        
        return data
    
    
class RegisteredCoursesSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer()
    course = CourseSerializer()
    class Meta:
        model = RegisteredCourses
        fields = ['id', 'student', 'course']
        
        
class ExamMaterialSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=True)
    title = serializers.CharField(required=True)
    file = serializers.FileField(required=True)

    class Meta:
        model = ExamMaterial
        fields = ['course', 'title', 'description', 'file']

class ExamReevaluationRequestSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer()
    exam = ExamSerializer
    class Meta:
        model = ExamReevaluationRequest
        fields = ['student', 'exam', 'request_date', 'feedback', 'status']
        
class ExamMarkTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'taken']
        
        
        
        
        
        
        
        
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'full_name', 'email', 'role']

# class SupervisorProfileSerializer(serializers.ModelSerializer):
#     exams_supervised = CustomUserSerializer(many=True, read_only=True)

#     class Meta:
#         model = SupervisorProfile
#         fields = ['id', 'supervisor', 'department', 'employee_id', 'job_title', 'exams_supervised']