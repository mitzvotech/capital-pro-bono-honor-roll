from django.conf.urls import patterns, include, url
from .views import HonoreeView, HonoreeCreate, HonoreeUpdate, HonoreeDelete
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'honorroll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'honoree/view/$', HonoreeView.as_view(), name='honoree_view'),
    url(r'honoree/add/$', HonoreeCreate.as_view(), name='honoree_add'),
    url(r'honoree/(?P<pk>[0-9]+)/$', HonoreeUpdate.as_view(), name='honoree_update'),
    url(r'honoree/(?P<pk>[0-9]+)/delete/$', HonoreeDelete.as_view(), name='honoree_delete')
)
