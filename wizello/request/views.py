from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Request, User
from account.models import Employee

# -------------------- Request List


class RequestListView(LoginRequiredMixin, ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request/requestlist.html"

    def get_queryset(self):
        qs = Request.objects.filter(
            user=self.request.user)
        return qs


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    fields = ('organization', 'position')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("request:requestlist")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("request:requestlist")

# -------------------- Request Manager List


class RequestManagerListView(LoginRequiredMixin, ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request/requestmanagerlist.html"

    def get_queryset(self):
        organization = self.request.user.employee.organization
        qs = Request.objects.filter(
            organization=organization).exclude(user=self.request.user).exclude(Q(user__employee__organization=organization) | Q(position="M"))
        return qs


class RequestManagerAcceptView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_request = get_object_or_404(Request, pk=pk)
        obj_request.agreement = timezone.now()

        objEmployee = Employee.objects.get(user=obj_request.user)
        objEmployee.position = obj_request.position
        objEmployee.organization = obj_request.organization
        objEmployee.save()

        obj_request.save()
        return HttpResponseRedirect(reverse_lazy("request:requestmanagerlist"))


# -------------------- Request Admin List
class RequestAdminListView(LoginRequiredMixin, ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request/requestadminlist.html"

    def get_queryset(self):
        qs = Request.objects.filter(
            position="M").filter(user__employee__organization=None)
        return qs


class RequestAdminAcceptView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_request = get_object_or_404(Request, pk=pk)
        obj_request.agreement = timezone.now()

        objEmployee = Employee.objects.get(user=obj_request.user)
        objEmployee.position = obj_request.position
        objEmployee.organization = obj_request.organization
        objEmployee.save()

        obj_request.save()
        return HttpResponseRedirect(reverse_lazy("request:requestadminlist"))
