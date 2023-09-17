from django.contrib import admin
from .models import User,Report,OrgUser


admin.site.register(User)
admin.site.register(Report)
admin.site.register(OrgUser)

