from core.models import BaseModel, models
from django.contrib.auth.models import User
from organization.models import Organization
from account.models import Employee


class Request(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    POSITION_TYPE = (
        ('M', "Manager"),
        ('EO', "Employee Organization"),
    )
    position = models.CharField(
        max_length=15, choices=POSITION_TYPE, default='EO')
    agreement = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"
        ordering = ['-created']

    def __str__(self):
        return "{} to {}".format(self.user.username, self.position)

    def get_request_status(self):
        if self.agreement:
            return "Verify"
        return "-"
