from django.contrib import admin
from .models import Employee,EmployeeLeave

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeLeave)