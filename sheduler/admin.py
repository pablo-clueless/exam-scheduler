from django.contrib import admin
from .models import CustomUser, Faculty, Department, Course, Exam, RegisteredCourses, SupervisorProfile, ExamOfficerProfile, StudentProfile, ExamAttendance

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
    list_display = ['id', 'course_name', 'description']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'date_time', 'get_supervisors', 'venue', 'exam_officer']

    def get_supervisors(self, obj):
        return ", ".join([str(supervisor) for supervisor in obj.supervisors.all()])
    get_supervisors.short_description = 'Supervisors'

@admin.register(SupervisorProfile)
class SupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'supervisor',  'department', 'employee_id', 'job_title']

@admin.register(ExamOfficerProfile)
class ExamOfficerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam_officer', 'department', 'employee_id', 'job_title']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_reg_number', 'student', 'department', 'matriculated', 'level', 'reg_year']

@admin.register(ExamAttendance)
class ExamAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'exam', 'student', 'attended']



@admin.register(RegisteredCourses)
class RegisteredCoursesAdmin(admin.ModelAdmin):
    list_display = ['student', 'course']