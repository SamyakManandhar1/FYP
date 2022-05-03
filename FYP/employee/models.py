from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from admins.models import CustomUser

# Create your models here.

SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
OTHERS= 'Other'

LEAVE_TYPE = (
    (SICK, 'Sick Leave'),
    (CASUAL, 'Casual Leave'),
    (EMERGENCY, 'Emergency Leave'),
    (OTHERS, 'Others'),
)


class Leave (models.Model):
    STATUS = (('approved', 'APPROVED'), ('unapproved',
              'UNAPPROVED'), ('decline', 'DECLINED'))

    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(
        choices=STATUS,  default='Not Approved', max_length=15)
    leavetype = models.CharField(
        choices=LEAVE_TYPE, max_length=25, default=SICK, null=True, blank=False)
    reason = models.CharField(verbose_name=_('Reason for Leave'), max_length=500,
                              help_text='Add additional information for leave', null=False, blank=False)

    def __str__(self):
        return self.employee + ' ' + self.start
