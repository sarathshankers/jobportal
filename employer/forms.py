from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
# user creation form
from django.contrib.auth.forms import UserCreationForm

                         # using normal form

# class JobForm(forms.Form):
#     job_title_name = forms.CharField()
#     company_name = forms.CharField()
#     location = forms.CharField()
#     salary = forms.IntegerField()
#     experience = forms.IntegerField()


                         # now using model form --------

class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs

        fields="__all__"





class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

#  password reset

# class PasswordResetForm(forms.Form):
#     password1=forms.CharField(widget=forms.PasswordInput())
#     confirm_password=forms.CharField()
#
#     def clean(self):
#         cleaned_data=super().clean()
#         pwd1=cleaned_data.get("password1")
#         pwd2=cleaned_data.get("confirm_password")
#         if pwd1 !=pwd2:
#             msg="password missmatch"
#             self.add_error("password1",msg)
#
# class CompanyProfileForm(forms.ModelForm):
#     class Meta:
#         model=CompanyProfile
#         exclude=("user",)
