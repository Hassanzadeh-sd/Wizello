from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"


class IndexView(TemplateView):
    template_name = "core/index.html"
