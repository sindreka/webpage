from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^$', 'startpage.views.StartpageView', name='Start page'),
#    url(r'^startpage', 'startpage.views.FrontpageView', name='Start page'),
#    url(r'^news/', include('polls.urls', namespace="polls")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]