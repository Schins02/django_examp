from django.conf.urls import patterns, url
from austin_grooves import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),)