from django.urls import path, include
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TaskManagerListView, TaskManagerCreateView, TaskManagerUpdateView, TaskManagerDeleteView)

app_name = 'task'

urlpatterns = [
    # task
    path('', TaskListView.as_view(), name="tasklist"),
    path('create/', TaskCreateView.as_view(), name="taskcreate"),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name="taskupdate"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="taskdelete"),
    # manager
    path('manager/', TaskListView.as_view(), name="taskmanagerlist"),
    path('manager/create/', TaskCreateView.as_view(), name="taskmanagercreate"),
    path('manager/edit/<int:pk>/', TaskListView.as_view(),
         name="taskmanagerupdate"),
    path('manager/delete/<int:pk>/',
         TaskListView.as_view(), name="taskmanagerdelete"),
]
