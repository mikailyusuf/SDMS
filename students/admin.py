from django.contrib import admin

# Register your models here.
from students.models import Teachers, Students

admin.site.register(Teachers)
admin.site.register(Students)
