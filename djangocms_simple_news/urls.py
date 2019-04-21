from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.SimpleNewsDetailView.as_view(), name="simple_news_detailview"),
    url(r'^cat/(?P<slug>[\w-]+)/$', views.SimpleNewsListView.as_view(), name="simple_news_listview"),
    url(r'^$', views.SimpleNewsListView.as_view(), name="simple_news_listview"),
]