from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Doubt
# Register your models here.
admin.site.register(Student)
admin.site.register(Doubt)