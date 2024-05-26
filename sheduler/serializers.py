from django.db import IntegrityError
from rest_framework import serializers
from .models import Course, CustomUser, ExamOfficerProfile, ExamSchedule, StudentProfile, SupervisorProfile
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


    
    
class ExamScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSchedule
        fields = ['id', 'course', 'date_time', 'venue', 'supervisors', 'exam_officer']

    def create(self, validated_data):
        supervisors_data = validated_data.pop('supervisors')
        exam_officer_data = validated_data.pop('exam_officer')

        exam_schedule = ExamSchedule.objects.create(**validated_data)

        exam_schedule.supervisors.set(supervisors_data)
        exam_schedule.exam_officer = exam_officer_data
        exam_schedule.save()

        return exam_schedule

    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.venue = validated_data.get('venue', instance.venue)

        supervisors_data = validated_data.get('supervisors')
        if supervisors_data:
            instance.supervisors.set(supervisors_data)

        exam_officer_data = validated_data.get('exam_officer')
        if exam_officer_data:
            instance.exam_officer = exam_officer_data

        instance.save()

        return instance


class SupervisorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorProfile
        fields = ['id', 'supervisor_name', 'exam', 'department', 'employee_id', 'job_title']


class ExamOfficerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamOfficerProfile
        fields = ['id', 'exam_officer_name', 'exam', 'department', 'employee_id', 'job_title']


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'student_reg_number', 'student_name', 'course', 'department', 'matric', 'year']
        
        
class CourseRegistrationSerializer(serializers.Serializer):
    student_id = serializers.UUIDField()
    course_id = serializers.UUIDField()

    def create(self, validated_data):
        student = StudentProfile.objects.get(id=validated_data['student_id'])
        course = Course.objects.get(id=validated_data['course_id'])
        student.course = course
        student.save()
        return student