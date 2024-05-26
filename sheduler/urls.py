from django.urls import path
from .views import (
    CourseRegistrationAPIView,
    CreateExamSchedule,
    RegisterUserAPIView,
    UpdateExamSchedule,
    UpdateSupervisorProfile, 
    UpdateExamOfficerProfile, 
    UpdateStudentProfile,
    
    UserLoginAPIView,
    
    ListSupervisorProfiles,
    ListExamOfficerProfiles,
    ListStudentProfiles,
)
urlpatterns = [
    path('create_user/', RegisterUserAPIView.as_view(), name='create_user'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    
    path('update-supervisor/<uuid:profile_id>/', UpdateSupervisorProfile.as_view(), name='update_supervisor_profile'),
    path('update-exam-officer/<uuid:profile_id>/', UpdateExamOfficerProfile.as_view(), name='update_exam_officer_profile'),
    path('update-student/<uuid:profile_id>/', UpdateStudentProfile.as_view(), name='update_student_profile'),
    
    
    path('list-supervisor-profiles/', ListSupervisorProfiles.as_view(), name='list_supervisor_profiles'),
    path('list-exam-officer-profiles/', ListExamOfficerProfiles.as_view(), name='list_exam_officer_profiles'),
    path('list-student-profiles/', ListStudentProfiles.as_view(), name='list_student_profiles'),
    
    
    path('create-exam-schedule/', CreateExamSchedule.as_view(), name='create_exam_schedule'),
    path('update-exam-schedule/<uuid:pk>/', UpdateExamSchedule.as_view(), name='update_exam_schedule'),
    
    
    path('course-registration/', CourseRegistrationAPIView.as_view(), name='course_registration'),
]
