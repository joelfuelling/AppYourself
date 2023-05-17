from django.forms import ModelForm
from .models import FollowUp, Role, SALARIES
from django import forms 
#? from .forms import SalaryChoiceField

class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ['name', 'contact', 'date']


# Salary stuff!
# class SalaryChoiceField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(choices=SALARIES, *args, **kwargs)

# class RoleForm(forms.ModelForm):
#     salary = SalaryChoiceField()

#     class Meta:
#         model = Role
#         fields = ['salary'] #? Is this correct?
