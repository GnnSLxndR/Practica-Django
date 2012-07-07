from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
	url(r'^$', 'index'),
	url(r'^question/$', 'question'),
	url(r'^delete/(?P<poll_id>\d+)/$', 'delete_question'),
	url(r'^detalle/(?P<poll_id>\d+)/$', 'detalle'),
	url(r'^actualizar/(?P<poll_id>\d+)/$', 'actualizar'),
	url(r'^new_choice/$', 'new_choice'),
	url(r'^new_choice2/(?P<poll_id>\d+)/$', 'new_choice2'),
	url(r'^(?P<poll_id>\d+)/$', 'detail1'),
	url(r'^(?P<poll_id>\d+)/results/$', 'results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
	url(r'^(?P<poll_id>\d+)/delete/$', 'delete_choice'),
)

