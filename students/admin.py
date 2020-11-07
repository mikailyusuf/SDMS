from django.contrib import admin

# Register your models here.
from students.models import Teachers, Students, Results

admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Results)
