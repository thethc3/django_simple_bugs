from . import views

__author__ = 'Thomas'
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^profile/(?P<username>\w+)/$', views.Profile.as_view(), name='profile'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^api/requirements/$', views.RequirementsApiList.as_view()),
    url(r'^api/requirements/(?P<pk>[0-9]+)/$', views.RequirementsAPIDetail.as_view()),
    url(r'^api/cases/$', views.CaseAPIList.as_view()),
    url(r'^api/cases/(?P<pk>[0-9]+)/$', views.CaseAPIDetail.as_view()),
    url(r'^api/cases/test-cases/(?P<pk>[0-9]+)/$', views.TestCaseDetail.as_view()),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)