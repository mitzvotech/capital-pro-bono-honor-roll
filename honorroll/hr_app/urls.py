from django.conf.urls import *  # NOQA
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic import ListView, CreateView, UpdateView
from hr_app import views, models
from models import Honoree
from tastypie.api import Api
from hr_app.api import HonorResource, HonoreeResource

v1_api = Api(api_name='v1')
v1_api.register(HonoreeResource())
v1_api.register(HonorResource())

urlpatterns = [
    url(r'^$', views.home),  # NOQA
    url(r'^admin/', include(admin.site.urls)),  # NOQA
	url(r'^organization/list$', views.show_organizations),
	url(r'^organization/detail/(?P<org_id>[0-9]+)/$', views.show_organization_detail, name="organization-detail"),
	url(r'^honorees/$', views.show_honorees),
	url(r'^honorees/detail/(?P<pk>[0-9]+)/$', UpdateView.as_view(model=Honoree), name='honoree-detail'),
	url(r'^honors/$', views.show_honors),
	url(r'^upload/$', views.uploadCSV),
    # url(r'^api/honoree/(?P<pk>[0-9]+)/$', views.HonoreeDetailView.as_view(), name='honoree-view'),
	url(r'^create/', views.AddOrgHonoreeHonorForm),
	url(r'^api/', include(v1_api.urls)),
	url(r'^search/', include('haystack.urls')),
]