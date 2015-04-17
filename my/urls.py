from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser import urls


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(urls)),
)

if settings.DEBUG or settings.ENABLE_MEDIA:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % getattr(settings, 'MEDIA_URL', '/')[1:], 'django.views.static.serve',
        {'document_root': getattr(settings, 'MEDIA_ROOT', '/dev/null'),  'show_indexes': True}),
    )
