from django.contrib import admin
from .models import User
from .models import Service,ServiceType


admin.site.register(User)
admin.site.register(Service)
admin.site.register(ServiceType)
