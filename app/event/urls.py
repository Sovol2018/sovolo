from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='event'

urlpatterns = [
    # event/
    url(r'^$', views.EventIndexView.as_view(), name='index'),
    # event/1/detail
    url(r'^(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='detail'),
    # event/1/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='delete'),
    # event/1/edit/
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EventEditView.as_view(), name='edit'),
    # event/1/participants/
    url(r'^(?P<event_id>[0-9]+)/participants/$', views.EventParticipantsView.as_view(), name='participants'),
    # event/add
    url(r'^add/$', views.EventCreate.as_view(), name='add'),
    # event/search
    url(r'^search/$', views.EventSearchResultsView.as_view(), name='search'),
    # event/participate
    url(r'^(?P<event_id>[0-9]+)/participate/$', views.event_participate, name='participate'),
    # event/1/cancel
    url(r'^(?P<pk>[0-9]+)/cancel/$', views.ParticipationDeleteView.as_view(), name='cancel'),
    # event/1/comment
    url(r'^(?P<event_id>[0-9]+)/comment/$', views.CommentCreate.as_view(), name='comment'),

]
