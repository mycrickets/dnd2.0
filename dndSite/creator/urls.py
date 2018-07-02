from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^creator/([\s\w]+)/$', views.detail, name='detail')
]
