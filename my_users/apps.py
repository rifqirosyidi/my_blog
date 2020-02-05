from django.apps import AppConfig


class MyUsersConfig(AppConfig):
    name = 'my_users'

    def ready(self):
        import my_users.signals
