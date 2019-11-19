from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Request, User

# -------------------- Request List


class RequestManagerListView(LoginRequiredMixin, ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request/requestmanagerlist.html"

    def get_queryset(self):
        organization = self.request.user.employee.organization
        qs = Request.objects.filter(
            organization=organization).exclude(user=self.request.user)
        return qs


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

        if form.cleaned_data['position'] == "M":
            print("Form_Manager")
        elif form.cleaned_data['position'] == "EO":
            print("Form_EmployeeOrganization")

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class RequestManagerAcceptView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_request = get_object_or_404(Request, pk=pk)
        obj_request.agreement = timezone.now()
        if obj_request.position == "M":
            print("Accept_Manager")
        elif obj_request.position == "EO":
            print("Accept_EmployeeOrganization")        
        obj_request.save()
        return HttpResponseRedirect(reverse_lazy("request:requestmanagerlist"))


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("request:requestlist")
