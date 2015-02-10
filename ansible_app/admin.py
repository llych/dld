from django.contrib import admin
from ansible_app.models import *

# Register your models here.
from kombu.transport.django import models as kombu_models

class TaskAdmin(admin.ModelAdmin):
    list_display=('task_id','status','created')
class TasksModuleAdmin(admin.ModelAdmin):
    list_display=('id','name','playbook','created')
admin.site.register(AnsibleTask,TaskAdmin)
admin.site.register(kombu_models.Message)

admin.site.register(TasksModule,TasksModuleAdmin)