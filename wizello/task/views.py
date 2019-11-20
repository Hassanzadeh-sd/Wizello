from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Task, User
from .forms import TaskManagerForm
# -------------------- Task List


class TaskListView(LoginRequiredMixin, ListView):
    context_object_name = "tasks"
    template_name = "task/tasklist.html"

    def get_queryset(self):
        qs = self.request.user.taskassignee.all()
        return qs


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('subject', 'description', 'deadline')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:tasklist")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        self.object.assignee.add(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('subject', 'description', 'deadline')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:tasklist")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("task:tasklist")


# -------------------- Task Manager List

class TaskManagerListView(LoginRequiredMixin, ListView):
    context_object_name = "tasks"
    template_name = "task/taskmanagerlist.html"

    def get_queryset(self):
        organization = self.request.user.employee.organization
        qs = Task.objects.filter(assignee__employee__organization=organization)
        return qs


class TaskManagerCreateView(LoginRequiredMixin, FormView):
    form_class = TaskManagerForm
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:taskmanagerlist")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        assignee = form.cleaned_data['ManagerAssignee']
        user_list = User.objects.filter(pk__in=assignee)
        for objuser in user_list:
            self.object.assignee.add(objuser)

        return HttpResponseRedirect(self.get_success_url())


class TaskManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('deadline', 'assignee')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:taskmanagerlist")


class TaskManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("task:taskmanagerlist")


# -------------------- Task Admin List

class TaskAdminListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/taskadminlist.html"


class TaskAdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('deadline', 'assignee')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:taskadminlist")


class TaskAdminDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("task:taskadminlist")
