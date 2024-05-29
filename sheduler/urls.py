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
    ExamMaterialAPIView,
    ExamReevaluationRequestAPIView,
    ExamScheduleCreateAPIView,
    FacultyCreateAPIView,
    FacultyUpdateView,
    ListCourses,
    MarkAttendanceAPIView,
    MarkExamTakenAPIView,
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
    ListDepartmentView,
    ListFacultyView,
)
urlpatterns = [
    path('create_user/', RegisterUserAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    
    path('faculties/create/', FacultyCreateAPIView.as_view()),
    path('faculties/', ListFacultyView.as_view()),
    path('faculties/update/<int:pk>/', FacultyUpdateView.as_view()),

    path('departments/create/', DepartmentCreateView.as_view()),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view()),
    path('departments', ListDepartmentView.as_view()),
    
    
    path('supervisors/update/<uuid:profile_id>/', UpdateSupervisorProfile.as_view()),
    path('supervisors/', ListSupervisorProfiles.as_view()),

    path('exam-officers/update/<uuid:profile_id>/', UpdateExamOfficerProfile.as_view()),
    path('exam-officers/', ListExamOfficerProfiles.as_view()),
    
    path('students/update/<uuid:profile_id>/', UpdateStudentProfile.as_view()),
    path('students/', ListStudentProfiles.as_view()),
    path('student/<uuid:student_id>/register-course/', CourseRegistrationAPIView.as_view()),
    path('student/<uuid:student_id>/registered-courses/', StudentRegisteredCoursesView.as_view()),
    path('student/<uuid:student_id>/exams/', StudentExamsView.as_view()),
    
    path('exam-schedules/create', ExamScheduleCreateAPIView.as_view()),
    path('exam-schedules/update/<uuid:pk>/', UpdateExamSchedule.as_view()),
    path('exam-schedules/', ExamListAPIView.as_view()),
    
    path('courses/create', CreateCourseAPIView.as_view()),
    path('courses/update/<uuid:course_id>/', UpdateCourseAPIView.as_view()),
    path('courses/', ListCourses.as_view()),
    
    path('supervisor-dashboard/', SupervisorDashboardAPIView.as_view()),
    path('mark-attendance/', MarkAttendanceAPIView.as_view()),
    
    path('courses/delete_all/', DeleteAllCoursesAPIView.as_view()),
    path('delete-attendance/', DeleteAllAttendances.as_view()),
    
    path('exam-materials/', ExamMaterialAPIView.as_view()),
    path('exam-reevaluation-requests/', ExamReevaluationRequestAPIView.as_view()),
    
    
    path('exam/<uuid:exam_id>/mark-taken/', MarkExamTakenAPIView.as_view()),
    
]
