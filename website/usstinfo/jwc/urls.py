#coding:utf-8
from django.conf.urls import url, include, handler404, handler500
from jwc import search_views
from jwc import views
from jwc import userinfo_view

handler404 = views.page_not_found
handler500 = views.internal_server_error
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$',search_views.MySearchView(),name='haystack_search'),
    url(r'^search/signin/$',userinfo_view.sign_in),
    url(r'^search/signup/$',userinfo_view.sign_up),
    url(r'^signin/$', userinfo_view.sign_in),
    url(r'^signup/$', userinfo_view.sign_up),
    url(r'^glances_add/$', views.glances_add),
    url(r'^signout/$', userinfo_view.sign_out)
]
