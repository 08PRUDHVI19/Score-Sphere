from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Semester)
# admin.site.register(CourseSemester)
admin.site.register(Result)
admin.site.register(SemResult)

