from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    job_title_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)
    def __str__(self):
         return self.job_title_name


# class CompanyProfile(models.Model):
#     company_name=models.CharField(max_length=120)
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employer")
#     logo=models.ImageField(upload_to="companyprofile",null=True)
#     location=models.CharField(max_length=120)
#     services=models.CharField(max_length=120)
#     description=models.CharField(max_length=200)




