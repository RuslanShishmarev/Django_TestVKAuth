from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile_detail, name='profile_detail'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_detail, name='profile_detail_with_pk'),
]