from django.apps import AppConfig


class ShedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sheduler'
    
    def ready(self):
        import sheduler.signals 
