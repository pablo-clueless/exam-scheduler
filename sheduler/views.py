from django.db import IntegrityError
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import status, permissions
from sheduler.models import CustomUser
from .serializers import  CourseRegistrationSerializer, CreateUserSerializer, ExamScheduleSerializer, LoginSerializer, SupervisorProfileSerializer, ExamOfficerProfileSerializer, StudentProfileSerializer
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .models import ExamSchedule, SupervisorProfile, ExamOfficerProfile, StudentProfile
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from knox.models import AuthToken


class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({"message": "User created successfully!", "user": serializer.data}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "User with this email or mobile number already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginAPIView(KnoxLoginView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name,
                'role': user.role,  
            },
            'token': token,
        })
    

class ListSupervisorProfiles(ListAPIView):
    queryset = SupervisorProfile.objects.all()
    serializer_class = SupervisorProfileSerializer
    
    
class ListExamOfficerProfiles(ListAPIView):
    queryset = ExamOfficerProfile.objects.all()
    serializer_class = ExamOfficerProfileSerializer
    
    
class ListStudentProfiles(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class UpdateSupervisorProfile(APIView):
    def put(self, request, profile_id):
        try:
            profile = SupervisorProfile.objects.get(pk=profile_id)
        except SupervisorProfile.DoesNotExist:
            return Response({"error": "Supervisor Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SupervisorProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class UpdateExamOfficerProfile(APIView):
    def put(self, request, profile_id):
        try:
            profile = ExamOfficerProfile.objects.get(pk=profile_id)
        except ExamOfficerProfile.DoesNotExist:
            return Response({"error": "Exam Officer Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ExamOfficerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class UpdateStudentProfile(APIView):
    def put(self, request, profile_id):
        try:
            profile = StudentProfile.objects.get(pk=profile_id)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class CreateExamSchedule(CreateAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer
    # permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        if self.request.user.role == 'exam_officer':
            serializer.save()
        else:
            raise permissions.PermissionDenied("You are not authorized to create exam schedules.")

    
class UpdateExamSchedule(UpdateAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer
    
    
    
class CourseRegistrationAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)