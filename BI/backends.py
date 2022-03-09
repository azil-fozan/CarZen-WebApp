from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class CustomLoginBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user_model = get_user_model()
        try:
            user = user_model._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None