#!coding:UTF-8
from django.contrib import admin

# Register your models here.
from host_management.models import *

class HostAdmin(admin.ModelAdmin):
    filter_vertical=('group',)  #选择器 垂直

admin.site.register(Host,HostAdmin)
admin.site.register(Group)