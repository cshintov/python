from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_input/$', views.get_input, name='get_input'),
    url(r'^result/$', views.result, name='result'),
    url(r'^show_tweets/$', views.show_tweets, name='show_tweets'),
]

