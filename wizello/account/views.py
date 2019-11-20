from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import Employee, User, Organization

# -------------------- Account List


class EmployeeListView(LoginRequiredMixin, ListView):
    context_object_name = "employees"
    template_name = "account/accountlist.html"

    def get_queryset(self):
        organization = self.request.user.employee.organization
        qs = Employee.objects.filter(
            organization=organization).exclude(user=self.request.user)
        return qs


class EmployeeDeactiveView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_employee = get_object_or_404(Employee, pk=pk)
        obj_employee.organization = None
        obj_employee.save()
        return HttpResponseRedirect(reverse_lazy("account:employeelist"))


# -------------------- Register
class EmployeeRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("core:login")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password1)
        new_user.save()

        obj_new_user = User.objects.get(pk=new_user.id)
        objNewEmployee, created = Employee.objects.get_or_create(
            user=obj_new_user)
        objNewEmployee.position = "E"
        objNewEmployee.save()

        return super(EmployeeRegisterView, self).form_valid(form)
