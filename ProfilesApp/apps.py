from django.apps import AppConfig


from django.apps import AppConfig

class ProfilesAppConfig(AppConfig):
    name = 'ProfilesApp'

    def ready(self):
        import ProfilesApp.signals

