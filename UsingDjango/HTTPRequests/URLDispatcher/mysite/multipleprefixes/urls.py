from django.conf.urls import patterns, url

# URLS without prefix

'''
urlpatterns = patterns('',
	url(r'^$', 'multipleprefixes.views.app_index'),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'multipleprefixes.views.month_display'),
	url(r'^tag/(?P<tag>\w+)/$', 'blog.views.tag'),

	)
'''

#Multiple view prefixes

urlpatterns = patterns('multipleprefixes.views',
	url(r'^$', 'app_index'),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$)', 'month_display'),
	)

urlpatterns += patterns('weblog.views',
	url(r'^tag/(?P<tag>\w+)/$', 'weblog.views.tag'),
	)