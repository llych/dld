from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static 

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$',views.CodeIndex),
    url(r'^addproject/$',views.AddProject,name='addproject'),
    url(r'^delproject/$',views.DelProject,name='delproject'),

    

)

