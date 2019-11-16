from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy


# -------------------- Task List
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/tasklist.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('subject', 'description', 'deadline', 'assignee')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:tasklist")


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        assignee = form.cleaned_data['assignee']
        user_list = User.objects.filter(pk__in=assignee)
        for objuser in user_list:
            self.object.assignee.add(objuser)
            
        return HttpResponseRedirect(self.get_success_url())



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('subject', 'description', 'deadline', 'assignee')
    template_name = "core/formcreate.html"
    success_url = reverse_lazy("task:tasklist")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("task:tasklist")
