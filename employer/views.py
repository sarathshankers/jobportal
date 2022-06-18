from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView,FormView
from employer.models import Jobs,CompanyProfile
# Create your views here.
from employer.forms import JobForm,LoginForm,CompanyProfileForm


# user authentication import
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# signup form
from employer.forms import SignUpForm

class EmployerHomeView(View):
    def get(self,request):
        return render(request,"emp-home.html")


#
# class AddJobView(View):
#     def get(self,request):
#         form= JobForm()
#         return render(request,"emp-addjob.html",{"form":form})
#
#     def post(self,request):
#         form=JobForm(request.POST)
#         if form.is_valid():

            # normal form method but it is lengthy coding

             # jobname=form.cleaned_data.get("job_title_name")
             # companyname=form.cleaned_data.get("company_name")
             # location=form.cleaned_data.get("location")
             # salary=form.cleaned_data.get("salary")
             # experience=form.cleaned_data.get("experience")
             # Jobs.objects.create(
             #     job_title_name=jobname,
             #     company_name=companyname,
             #     location=location,
             #     salary=salary,
             #     experience=experience
             #    )

        #      form.save()
        #      return render(request,"emp-home.html")
        #     # return redirect("emp-alljobs")
        # else:
        #     return render(request, "emp-addjob.html", {"form": form})

# class ListJobView(View):
#
#     def get(self,request):
#         qs=Jobs.objects.all()
#         return render(request,"emp-listjob.html",{"jobs":qs})

#
# class JobDetailView(View):
#
#     def get(self, request,id):
#         qs=Jobs.objects.get(id=id)
#         return render(request, "emp_jobdetails.html", {"jobs": qs})
#
# class JobEditView(View):
#
#     def get(self, request,id):
#         qs=Jobs.objects.get(id=id)
#         form = JobForm(instance=qs)
#         return render(request, "emp-editjob.html", {"form": form})
#
#     def post(self, request, id):
#         qs = Jobs.objects.get(id=id)
#         form = JobForm(request.POST, instance=qs)
#         if form.is_valid():
#             form.save()
#             return redirect("emp-alljobs")
#         else:
#             return render(request, "emp-editjob.html", {"form": form})
#
#
# class JobDeleteview(View):
#     def get(self, request, id):
#         qs=Jobs.objects.get(id=id)
#         qs.delete()
#         return redirect("emp-alljobs")




# django already have a create view to create view jobs, a list view for list jobs



class ListJobView(ListView):
    model=Jobs
    context_object_name="jobs"
    template_name="emp-listjob.html"

    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)

class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    success_url = reverse_lazy("emp-alljobs")

    def form_valid(self, form):
        form.instance.company=self.request.user
        return super().form_valid(form)

class JobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "emp_jobdetails.html"
    pk_url_kwarg = "id"

class JobEditView(UpdateView):
    model=Jobs
    form_class=JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"


class JobDeleteView(DeleteView):
    model = Jobs
    template_name = "jobconfirmdelete.html"
    success_url = reverse_lazy("emp-alljpbs")
    pk_url_kwarg = "id"



# user registration


class SignUpView(CreateView):
    model =User
    form_class = SignUpForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("emp-alljobs")

class SignInView(FormView):
    form_class=LoginForm
    template_name='login.html'

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)

                return redirect("emp-alljobs")
            else:
                return render(request,"login.html",{"form":form})


#  logout
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


#   change password
class ChangePasswordView(TemplateView):
    template_name="changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")

        else:
            return render(request,self.template_name)
#

class PasswordResetView(TemplateView):

    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{{"msg":"Password Mismatch"}})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")
#


class CompanyProfileView(CreateView):
    model=CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-addprofile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form=CompanyProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("emp-home")
    #     else:
    #         return render(request,self.template_name,{"form":form})



class EmpViewProfileView(TemplateView):
    template_name = "emp-viewprofile.html"

class EmpProfileEditView(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-editprofile.html"
    success_url = reverse_lazy("emp-viewprofile")
    pk_url_kwarg = "id"

