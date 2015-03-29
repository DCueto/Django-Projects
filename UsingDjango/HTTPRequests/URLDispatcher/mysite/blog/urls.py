from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views
from . import ClassBasedView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>\d+)/$', views.page),
    url(r'^archive/$', views.archive),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^myview/$', ClassBasedView.as_view()),

)
