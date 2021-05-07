from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

# Script para o usuario logan com seu e-mail ao inves do username
class EmailUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(Q(email__exact=username))
            print(user.check_password(password))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
