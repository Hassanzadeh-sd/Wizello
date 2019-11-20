from django import forms
from .models import Task
from account.models import Employee


class TaskManagerForm(forms.Form):
    managerAssigneeChoices = []
    for objEmployee in Employee.objects.filter(pk=2):
        managerAssigneeChoices.append(
            [objEmployee.user.id, objEmployee.user.username])

    subject = forms.CharField(label="Subject", max_length=200)
    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'your Description',
                                             'class': 'form-control'}
                                  ))
    deadline = forms.DateTimeField(label="Deadline")
    ManagerAssignee = forms.SelectMultiple(choices=managerAssigneeChoices)
