from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CentralPrison)
admin.site.register(Prison)
admin.site.register(Criminal)
admin.site.register(Visitor)
admin.site.register(User)
admin.site.register(Image)