from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, SupervisorProfile, ExamOfficerProfile, StudentProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'supervisor':
            SupervisorProfile.objects.create(supervisor=instance)
        elif instance.role == 'exam_officer':
            ExamOfficerProfile.objects.create(exam_officer=instance)
        elif instance.role == 'student':
            StudentProfile.objects.create(student=instance)