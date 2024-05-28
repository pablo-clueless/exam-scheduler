from django.urls import path
from .background_jobs import start_background_tasks

# start_background_tasks()

from .views import (
    CourseRegistrationAPIView,
    CreateCourseAPIView,
    DeleteAllAttendances,
    DeleteAllCoursesAPIView,
    DepartmentCreateView,
    DepartmentUpdateView,
    ExamListAPIView,
    ExamScheduleCreateAPIView,
    FacultyCreateAPIView,
    FacultyUpdateView,
    ListCourses,
    MarkAttendanceAPIView,
    RegisterUserAPIView,
    StudentExamsView,
    StudentRegisteredCoursesView,
    SupervisorDashboardAPIView,
    UpdateCourseAPIView,
    UpdateExamSchedule,
    UpdateSupervisorProfile, 
    UpdateExamOfficerProfile, 
    UpdateStudentProfile,
    
    UserLoginAPIView,
    
    ListSupervisorProfiles,
    ListExamOfficerProfiles,
    ListStudentProfiles,
    StudentCoursesAPIView,
)
urlpatterns = [
    path('create_user/', RegisterUserAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    
    
    path('faculties/create/', FacultyCreateAPIView.as_view()),
    path('faculties/update/<int:pk>/', FacultyUpdateView.as_view()),
    path('departments/create/', DepartmentCreateView.as_view()),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view()),
    
    
    path('update-supervisor/<uuid:profile_id>/', UpdateSupervisorProfile.as_view()),
    path('update-exam-officer/<uuid:profile_id>/', UpdateExamOfficerProfile.as_view()),
    path('update-student/<uuid:profile_id>/', UpdateStudentProfile.as_view()),
    
    path('list-supervisor-profiles/', ListSupervisorProfiles.as_view()),
    path('list-exam-officer-profiles/', ListExamOfficerProfiles.as_view()),
    path('list-student-profiles/', ListStudentProfiles.as_view()),
    
    path('exam-schedule/', ExamScheduleCreateAPIView.as_view()),
    path('update-exam-schedule/<uuid:pk>/', UpdateExamSchedule.as_view()),
    path('list-exams/', ExamListAPIView.as_view()),
    
    
    
    path('create-course/', CreateCourseAPIView.as_view()),
    path('update-course/<uuid:course_id>/', UpdateCourseAPIView.as_view()),
    path('list-courses/', ListCourses.as_view()),
    
    
    path('student/<uuid:student_id>/register-course/', CourseRegistrationAPIView.as_view()),
    path('student/<uuid:student_id>/registered-courses/', StudentRegisteredCoursesView.as_view()),
    path('student/<uuid:student_id>/exams/', StudentExamsView.as_view()),
    
    path('supervisor-dashboard/', SupervisorDashboardAPIView.as_view()),
    path('mark-attendance/', MarkAttendanceAPIView.as_view()),
    
    path('courses/delete_all/', DeleteAllCoursesAPIView.as_view()),
    path('delete-attendance/', DeleteAllAttendances.as_view()),
    
]
