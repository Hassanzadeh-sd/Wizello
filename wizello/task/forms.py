from django import forms
from .models import Task
from account.models import Employee


class TaskManagerForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'subject',
            'description',
            'deadline',
            'assignee',
        ]

    def __init__(self, *args, **kwargs):
        super(TaskManagerForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs['class'] = 'datepicker'
