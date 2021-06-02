from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    """need to define ready to import signals"""

    def ready(self):
        import profiles.signals
