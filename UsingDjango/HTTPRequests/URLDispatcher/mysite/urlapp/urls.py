from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>\d{4})/$', views.year_archive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', views.article_detail),
)
