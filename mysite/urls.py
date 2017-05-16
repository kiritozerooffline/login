from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('mysite.core.urls')),
	url(r'^', include('mysite.dablog.urls')),
]