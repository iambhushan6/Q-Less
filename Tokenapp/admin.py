from django.contrib import admin
from Tokenapp.models import Student, CurrentToken

# Register your models here.
admin.site.register(Student)
admin.site.register(CurrentToken)