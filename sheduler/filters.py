import django_filters
from .models import Exam

class ExamFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='course__department__department_name', lookup_expr='icontains')
    course = django_filters.CharFilter(field_name='course__course_name', lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date_time', lookup_expr='date')
    venue = django_filters.CharFilter(field_name='venue', lookup_expr='icontains')

    class Meta:
        model = Exam
        fields = ['department', 'course', 'date', 'venue']