from django.apps import AppConfig

class AppTwoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_two'

    def ready(self):
        import app_two.signals
