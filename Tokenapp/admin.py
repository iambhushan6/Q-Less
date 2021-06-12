from django.contrib import admin
from Tokenapp.models import Student, CurrentToken, Alumni, AlumniCurrentToken

# Register your models here.
admin.site.register(Student)
admin.site.register(CurrentToken)
admin.site.register(Alumni)
admin.site.register(AlumniCurrentToken)