from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.main),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^dashboard$', views.dashboard),
	url(r'^add$', views.add),
	url(r'^addItem$', views.addItem),
	url(r'^show$', views.addItem),
	url(r'^wish_list/(?P<id>\d+)$', views.wish_list_item),

]