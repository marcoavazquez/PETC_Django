from django.conf.urls import patterns, url
from .views import PersonalView


urlpatterns = patterns('',
    url(r'^personal/$', PersonalView.as_view(), name="personal"),
    url(r'^personal/(?P<rfc>[\W\w]+)/$', PersonalView.as_view(), name="personal"),
)