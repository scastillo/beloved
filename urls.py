from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

from app.api import BelovedResource

beloved_api = Api(api_name='v1')
beloved_api.register(BelovedResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(beloved_api.urls))
    )
