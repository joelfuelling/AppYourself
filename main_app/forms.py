from django import forms
from .models import SALARIES, Role
# from .forms import SalaryChoiceField

# # Salary stuff!
# class SalaryChoiceField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(choices=SALARIES, *args, **kwargs)

# class RoleForm(forms.ModelForm):
#     salary = SalaryChoiceField()

#     class Meta:
#         model = Role
#         fields = '__all__'
# Salary stuff!