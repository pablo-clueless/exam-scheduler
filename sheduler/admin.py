from django.contrib import admin
from .models import CustomUser, Faculty, Department, Course, ExamSchedule, SupervisorProfile, ExamOfficerProfile, StudentProfile, ExamAttendance

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'role', 'email', 'created_at', 'updated_at', 'is_staff', 'is_superuser']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'faculty_name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'faculty', 'department_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'start_date', 'end_date']

@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'date_time', 'venue', 'exam_officer']

@admin.register(SupervisorProfile)
class SupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'supervisor_name', 'exam', 'department', 'employee_id', 'job_title']

@admin.register(ExamOfficerProfile)
class ExamOfficerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam_officer_name', 'exam', 'department', 'employee_id', 'job_title']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_reg_number', 'student_name', 'course', 'department', 'matric', 'year']

@admin.register(ExamAttendance)
class ExamAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam', 'student', 'attended']
