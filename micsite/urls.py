from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'micsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$',  'micsite.views.login'),
    (r'^logout/$',  'micsite.views.logout'),
    (r'^changepwd/$',  'micsite.views.changepwd'),
    (r'^index/$',  'micsite.views.index'),
    (r'^index/(?P<nodeid>\d+)/$','micsite.views.index'),
    (r'^$','micsite.views.login'),
    (r'^test/$',  'micsite.views.test'),
    (r'^test_view/$',  'micsite.views.test_view'),
)
