from django.contrib import admin
from .models import Role, FollowUp, Tag

# Register your models here.
admin.site.register(Role)
admin.site.register(FollowUp)
admin.site.register(Tag)
