from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static 

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$',views.Ansible_app),
    url(r'^addtask/$',views.AddTask,name="addtask"),
    url(r'^gettask/(?P<taskID>.*)/$',views.GetTask,name="gettask"),
    url(r'^getstatus/$',views.GetTaskStatus,name="getstatus"),
    url(r'^getmodule/$',views.GetAnsbileModule,name="getmodule"),
    url(r'^addModule/$',views.AddAnsbileModule,name="addModule"),
    url(r'^delModule/$',views.DelAnsbileModule,name="delModule"),
    url(r'^upModule/$',views.UpAnsbileModule,name="upModule"),
    

)

