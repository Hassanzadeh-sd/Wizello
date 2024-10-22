from django.urls import path, include
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TaskManagerListView, TaskManagerCreateView, TaskManagerUpdateView, TaskManagerDeleteView,
    TaskAdminListView, TaskAdminUpdateView, TaskAdminDeleteView)

app_name = 'task'

urlpatterns = [
    # task
    path('', TaskListView.as_view(), name="tasklist"),
    path('create/', TaskCreateView.as_view(), name="taskcreate"),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name="taskupdate"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="taskdelete"),
    # manager
    path('manager/', TaskManagerListView.as_view(), name="taskmanagerlist"),
    path('manager/create/', TaskManagerCreateView.as_view(),
         name="taskmanagercreate"),
    path('manager/edit/<int:pk>/', TaskManagerUpdateView.as_view(),
         name="taskmanagerupdate"),
    path('manager/delete/<int:pk>/',
         TaskManagerDeleteView.as_view(), name="taskmanagerdelete"),
    # admin
    path('admin/', TaskAdminListView.as_view(), name="taskadminlist"),
    path('admin/edit/<int:pk>/', TaskAdminUpdateView.as_view(),
         name="taskadminupdate"),
    path('admin/delete/<int:pk>/',
         TaskAdminDeleteView.as_view(), name="taskadmindelete"),
]
