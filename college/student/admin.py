from django.contrib import admin

# Register your models here.


from .models import Student,Subject,Mark,Course,Attendence

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(Attendence)