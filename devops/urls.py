from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static 

import settings
import login_admin.views,host_management.views,ansible_app.urls,code_management.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login_admin.views.LoginView),
    url(r'^$',login_admin.views.Index),
    url(r'^logout/$',login_admin.views.Logout,name='logout'),
    url(r'^host/$',host_management.views.HostManagement),
    url(r'^addhost/$',host_management.views.AddHost,name="addhost"),
    url(r'^gethost/$',host_management.views.GetHost,name="gethost"),
    url(r'^delhost/$',host_management.views.DelHost,name="delhost"),
    url(r'^uphost/$',host_management.views.UpHost,name="uphost"),
    url(r'^ansible/', include(ansible_app.urls)),
    url(r'^code/', include(code_management.urls)),
)

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT ) 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT ) 