from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, View, DeleteView
from .models import Request, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy


# -------------------- Request List
class RequestListView(LoginRequiredMixin, ListView):
    model = Request
    context_object_name = "requests"
    template_name = "request/requestlist.html"


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


class RequestAcceptView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        obj_request = get_object_or_404(Request, pk=pk)
        # check permission
        obj_request.agreement = timezone.now()
        obj_request.save()
        return HttpResponseRedirect(reverse_lazy("request:requestlist"))


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("request:requestlist")
