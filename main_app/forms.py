from django.forms import ModelForm
from .models import FollowUp, Role, SALARIES
from django import forms 
from django.contrib.auth.models import User
#? from .forms import SalaryChoiceField

class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ['name', 'contact', 'date']

# user 'Sign Up' authentication... What about passing these to a 'Profile' Form as well?
# urls.py would need 'add_user' or something similar to 'add_feeding' in cats model
#! class RegistrationForm(ModelForm):
#!     class Meta:
#!         model = User
#!         fields = ['username', 'email', 'first_name', 'last_name', 'password']
#!         # How to implement 'confirm_password' might get tricky (GOOGLE IT)

#!         def is_valid(self):
#!             if(self.instance.confirm_password != self.instance.password):
#!                 return False
#!             return True
        
# Salary stuff!
# class SalaryChoiceField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(choices=SALARIES, *args, **kwargs)

# class RoleForm(forms.ModelForm):
#     salary = SalaryChoiceField()

#     class Meta:
#         model = Role
#         fields = ['salary'] #? Is this correct?
