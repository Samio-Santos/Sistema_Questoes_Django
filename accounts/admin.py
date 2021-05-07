from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CostumerUser

admin.site.register(CostumerUser, auth_admin.UserAdmin)