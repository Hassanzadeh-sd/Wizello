from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, View
from .models import Employee, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import RegisterForm

# -------------------- Account List


class AccountListView(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "account/accountlist.html"


class AccountDeactiveView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_employee = get_object_or_404(Employee, pk=pk)
        # check permission
        obj_employee.organization = 1
        obj_employee.save()
        return HttpResponseRedirect(reverse_lazy("account:accountlist"))


# -------------------- Register
class RegisterView(FormView):
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

        obj_new_user = User.objects.get(username=username)
        obj_user_employee, created = Employee.objects.get_or_create(
            user=obj_new_user)
        try:
            obj_user_employee.organization = form.cleaned_data['organization']
        except:
            pass
        obj_user_employee.save()

        return super(RegisterView, self).form_valid(form)
