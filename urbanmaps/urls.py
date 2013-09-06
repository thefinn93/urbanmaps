from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from urbanmaps import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^info/', views.info),
    url(r'^admin/', include(admin.site.urls)),
)
