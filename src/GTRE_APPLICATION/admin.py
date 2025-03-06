#admin.py


from django.contrib import admin
from GTRE_APPLICATION.models import MainAdmin
from GTRE_APPLICATION.models import *

# Register your models here.

admin.site.register(MainAdmin)
admin.site.register(SubAdmin)
admin.site.register(Room)
admin.site.register(Alert)