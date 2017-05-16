from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^postlist', views.postlist, name='postlist'),
	url(r'^post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]