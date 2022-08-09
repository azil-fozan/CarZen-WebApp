from django.contrib import admin

# Register your models here.
from BI.models import User
from user_profiles.models import MechanicDetail

admin.site.register(User)
# admin.site.register(MechanicDetail)
