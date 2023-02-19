# Code derived from "Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture" Timestamp 32:31
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
