from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^urlapp/', include(urlapp.urls, namespace='urlapp')),
    url(r'^blog/', include(blog.urls, namespace='blog')),
    url(r'^news/', include(news.urls, namespace='news')),
    url(r'^multipleprefixes/', include(multipleprefixes.urls, namespace='multipleprefixes')),

)
