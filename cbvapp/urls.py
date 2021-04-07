from django.conf.urls import url
from cbvapp import views

app_name='cbvapp'

urlpatterns = [
    url(r'^$',views.schoollistview.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.schooldetailview.as_view(),name='detail'),
    url(r'^create/$',views.schoolcreateview.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.schoolupdateview.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.schooldeleteview.as_view(),name='delete'),

]
