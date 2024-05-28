# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.utils import timezone
from datetime import timedelta
from django.db import close_old_connections
from ..models import Exam, StudentProfile
from ..utils import send_exam_reminder_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

def send_exam_reminders():
    close_old_connections() 

    upcoming_exams = Exam.objects.all()
    # upcoming_exams = Exam.objects.filter(date_time__range=[timezone.now(), timezone.now() + timedelta(seconds=10)])
    
    for exam in upcoming_exams:
        students = StudentProfile.objects.filter(registeredcourses__course=exam.course)
        for student in students:
            send_exam_reminder_email('devcaliban@gmail.com', exam.course.course_name, exam.date_time)
            
    print(upcoming_exams)

    close_old_connections() 

@register_job(scheduler, "interval", seconds=10)
def scheduled_job():
    send_exam_reminders()

register_events(scheduler)

def start():
    scheduler.start()
