from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^login/$', auth_views.login),
	url(r'^logout/$', views.logout_view),
]
