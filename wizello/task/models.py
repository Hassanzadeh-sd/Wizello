from core.models import BaseModel, models
from django.contrib.auth.models import User


class Task(BaseModel):
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    deadline = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ManyToManyField(User, related_name='taskassignee')

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['deadline']

    def __str__(self):
        return self.subject

    def get_assignee(self):
        assigneeNames = ""
        for objAssignee in self.assignee.all():
            assigneeNames += objAssignee.username + " , "
        return assigneeNames
