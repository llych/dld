from django.db import models

from host_management.models import *
from django.utils.translation   import ugettext_lazy as _
# Create your models here.

class AnsibleTask(models.Model):
    task_id = models.CharField(max_length=50,unique=True)
    host=models.ManyToManyField(Host)
    created  = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))
    status=models.CharField(max_length=20,blank=True, null=True)
    info=models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.task_id

class TasksModule(models.Model):
    
    name = models.CharField(max_length=50)
    playbook = models.CharField(max_length=200)
    created  = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))
    
    info = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.name