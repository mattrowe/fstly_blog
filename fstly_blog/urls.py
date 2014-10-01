from django.conf.urls import patterns, include, url
from django.contrib import admin
from fstly_blog.views import HomeView, DetailView, EditView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="HomeView"),
    url(r'^detail/(?P<slug>\w+)/$', DetailView.as_view(), name="DetailView"),
    url(r'^edit/(?P<post_id>[0-9]+)/$', EditView.as_view(), name="EditView"),
    url(r'^edit/$', EditView.as_view(), name="ComposeView"),
    url(r'^admin/', include(admin.site.urls)),
)
