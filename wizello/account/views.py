from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, View
from .models import Employee, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy


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
