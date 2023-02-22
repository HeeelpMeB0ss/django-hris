from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import EmployeeForm, EmployeeLeaveForm
from .models import Employee, EmployeeLeave

# Create your views here.
class CreateEmployeeLeave(LoginRequiredMixin, generic.CreateView):
    form_class = EmployeeLeaveForm
    template_name = "employee/employee_leave.html"
    success_url = reverse_lazy("employee:index")
    context_object_name = "employee_leave"

class CreateEmployee(LoginRequiredMixin, generic.CreateView):
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")
    context_object_name = "create_employee"


class UpdateEmployee(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("employee:index")
    context_object_name = "update_employee"


class DeleteEmployee(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employee:index")
    template_name = "employee/delete_form.html"
    context_object_name = "delete_employee"


class EmployeeListView(generic.ListView):
    model = Employee
    template_name = "employee/list_view.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("employee:index")
    template_name = "employee/signup.html"

class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    template_name = "employee/detail_view.html"