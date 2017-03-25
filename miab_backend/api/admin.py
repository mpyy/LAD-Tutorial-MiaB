from django.contrib import admin

# Register your models here.
from . import models

# Register our "Message" model with the Django Admin/
admin.site.register(models.Message)
