from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status, permissions
from sheduler.filters import ExamFilter
from django_filters.rest_framework import DjangoFilterBackend
from sheduler.models import CustomUser
from sheduler.permissions import IsExamOfficer, IsStudent, IsSupervisor
from .serializers import  (
    AttendanceSerializer,
    CourseRegistrationSerializer, 
    CourseSerializer, 
    CreateUserSerializer, 
    DepartmentSerializer,
    ExamMarkTakenSerializer,
    ExamMaterialSerializer,
    ExamReevaluationRequestSerializer, 
    ExamSerializer, 
    FacultySerializer, 
    LoginSerializer,
    RegisteredCoursesSerializer, 
    SupervisorProfileSerializer, 
    ExamOfficerProfileSerializer, 
    StudentProfileSerializer
    )
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .models import (
    Course, 
    Department, 
    Exam,
    ExamAttendance,
    ExamMaterial,
    ExamReevaluationRequest, 
    Faculty, 
    RegisteredCourses, 
    SupervisorProfile, 
    ExamOfficerProfile, 
    StudentProfile
) 
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
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
    
class CreateCourseAPIView(APIView):
    permission_classes = [IsExamOfficer]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCourseAPIView(APIView):
    permission_classes = [IsExamOfficer]

    def put(self, request, course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListCourses(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
        
        
class FacultyCreateAPIView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def create(self, request, *args, **kwargs):
        faculties_data = request.data.get('faculties', [])
        for faculty_data in faculties_data:
            faculty_serializer = FacultySerializer(data=faculty_data)
            if faculty_serializer.is_valid():
                faculty_serializer.save()
            else:
                return Response(faculty_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Faculties created successfully'}, status=status.HTTP_201_CREATED)


class FacultyUpdateView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.get('departments', [])
        if not isinstance(data, list):
            return Response({"error": "Expected a list of data"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = DepartmentSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentUpdateView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
        
        
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
            profile = SupervisorProfile.objects.get(id=profile_id)
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
            profile = ExamOfficerProfile.objects.get(id=profile_id)
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
            profile = StudentProfile.objects.get(id=profile_id)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    
class ExamScheduleCreateAPIView(CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated, IsExamOfficer]

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, ValidationError):
            response.data = {'errors': response.data}
        return response


class ExamListAPIView(ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExamFilter


class UpdateExamSchedule(UpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated, IsExamOfficer, IsSupervisor]

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, ValidationError):
            response.data = {'errors': response.data}
        return response
    
    
    
class CourseRegistrationAPIView(CreateAPIView):
    queryset = RegisteredCourses.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def create(self, request, *args, **kwargs):
        student_id = self.kwargs.get('student_id')

        # Get the student's profile
        student_profile = get_object_or_404(StudentProfile, id=student_id)

        # Add the student profile to the request data
        request.data['student'] = str(student_profile.id)

        return super().create(request, *args, **kwargs)

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if isinstance(exc, ValidationError):
            response.data = {'errors': response.data}
        return response
    
    
class StudentCoursesAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request):
        courses = Course.objects.filter(studentprofile__student_name=request.user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    
class StudentRegisteredCoursesView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request, student_id):
        # Fetch the student profile using the provided student ID
        student = get_object_or_404(StudentProfile, id=student_id)
        # Get the registered courses for the student
        registered_courses = RegisteredCourses.objects.filter(student=student)
        # Serialize the registered courses data
        serializer = RegisteredCoursesSerializer(registered_courses, many=True)
        return Response(serializer.data)


class MarkAttendanceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSupervisor]

    def post(self, request, *args, **kwargs):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class DeleteAllAttendances(APIView):
    def delete(self, request, *args, **kwargs):
        # Delete all instances of ExamAttendance
        count, _ = ExamAttendance.objects.all().delete()
        return Response(
            {"message": f"Deleted {count} attendance records."},
            status=status.HTTP_204_NO_CONTENT
        )

class SupervisorDashboardAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSupervisor]
    serializer_class = ExamSerializer

    def get_queryset(self):
        user = self.request.user
        return Exam.objects.filter(supervisors__supervisor=user)
    
    
class DeleteAllCoursesAPIView(APIView):
    
    """
    View to delete all courses in the system.
    Only accessible by exam officers.
    """
    permission_classes = [permissions.IsAuthenticated, IsSupervisor]

    def delete(self, request):
        Course.objects.all().delete()
        return Response({"message": "All courses have been deleted."}, status=status.HTTP_204_NO_CONTENT)


class StudentExamsView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get(self, request, student_id):
        # Fetch the student profile using the provided student ID
        student = get_object_or_404(StudentProfile, id=student_id)
        # Fetch exams for the student
        exams = RegisteredCourses.objects.get_exams_for_student(student)
        # Prepare the response data
        exam_data = [
            {
                'course': exam.course.course_name,
                'exam_date_time': exam.date_time,
                'venue': exam.venue,
            } for exam in exams
        ]
        return Response(exam_data)
    
    
    
class ExamMaterialAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        materials = ExamMaterial.objects.all()
        serializer = ExamMaterialSerializer(materials, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamReevaluationRequestAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        reevaluation_requests = ExamReevaluationRequest.objects.filter(student=request.user.studentprofile)
        serializer = ExamReevaluationRequestSerializer(reevaluation_requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamReevaluationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user.studentprofile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class MarkExamTakenAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, exam_id, format=None):
        exam = get_object_or_404(Exam, id=exam_id)
        serializer = ExamMarkTakenSerializer(exam, data={'taken': True}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'exam marked as taken'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)