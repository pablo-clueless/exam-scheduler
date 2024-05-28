# utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_exam_reminder_email(student_email, course_name, exam_date_time):
    subject = 'Exam Reminder'
    html_message = render_to_string('exam_reminder.html', {'course_name': course_name, 'exam_date_time': exam_date_time})
    plain_message = strip_tags(html_message)
    from_email = 'Schooloftech@mail.com'
    recipient_list = [student_email, 'devaliban@gmail.com']
    
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)
