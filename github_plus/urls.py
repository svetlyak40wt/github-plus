from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'frontpage.html'}),
    url(r'^auth/login/$', 'github_plus.views.login', name='login'),
    url(r'^auth/logout/$', 'github_plus.views.logout', name='logout'),
    url(r'^auth/callback/$', 'github_plus.views.auth_callback', name='auth-callback'),
    # Examples:
    # url(r'^$', 'github_plus.views.home', name='home'),
    # url(r'^github_plus/', include('github_plus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
