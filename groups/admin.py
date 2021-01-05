from django.contrib import admin
from . import models

class GroupMember(admin.TabularInline):
    model = models.GroupMember 

admin.site.register(models.Group)
