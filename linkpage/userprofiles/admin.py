from django.contrib import admin

from .models import SocialLink
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(SocialLink)
