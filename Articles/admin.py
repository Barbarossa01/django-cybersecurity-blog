from django.contrib import admin

# Register your models here.
from .models import Profile,Article

admin.site.register(Profile)
admin.site.register(Article)
