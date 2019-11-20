from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Organization

# -------------------- Organization


class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = "organizations"
    template_name = "organization/organizationlist.html"


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ('__all__')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("organization:organizationlist")


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ('__all__')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("organization:organizationlist")


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("organization:organizationlist")
