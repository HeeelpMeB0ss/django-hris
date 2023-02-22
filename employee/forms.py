from django import forms


from .models import Employee, EmployeeLeave


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields  = '__all__'
        widgets = {
            'dateBirth': forms.DateInput(attrs={'type': 'date'}),
             'gender': forms.RadioSelect,
        }

class EmployeeLeaveForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeave
        fields = '__all__'
        widgets = {
            'date_leave': forms.DateInput(attrs={'type': 'date'}),
            'date_back': forms.DateInput(attrs={'type': 'date'}),
        }
