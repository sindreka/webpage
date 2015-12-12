from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^$', 'startpage.views.StartpageView', name='startpage'),
#    url(r'^startpage', 'startpage.views.FrontpageView', name='Start page'),
    url(r'^news/', 'news.views.NewsView', name='news' ),
    url(r'^polls/', 'polls.views.pollsView', name='polls'),
    url(r'^admin/', include(admin.site.urls)),
]