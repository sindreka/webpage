from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^home/$', 'startpage.views.home', name='startpage'),
	url(r'^$', 'startpage.views.home', name='startpage'),
	url(r'^about/$', 'startpage.views.about', name='startpage'),
	url(r'^recipes/$', 'startpage.views.home', name='startpage'),
	url(r'^private/$', 'startpage.views.home', name='startpage'),
	url(r'^contact/$', 'startpage.views.home', name='startpage'),
#    url(r'^startpage', 'startpage.views.FrontpageView', name='Start page'),
#    url(r'^news/', 'news.views.NewsView', name='news' ),
#    url(r'^polls/', 'polls.views.pollsView', name='polls'),
    url(r'^admin/', include(admin.site.urls)),
]