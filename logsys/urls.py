__author__ = 'ads18'
from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Car_shop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^login/', 'logsys.views.login'),
                       url(r'^logout/', 'logsys.views.logout'),
                       url(r'^register/','logsys.views.register')
                        )