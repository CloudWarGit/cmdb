from django.conf.urls import url
from assets.views import *

urlpatterns = [
    url(r'^$', AssetsView.as_view(), name="overview"),
    url(r'hosts/$', HostsView.as_view(template_name='assets/hosts_list.html'), name='hosts-list'),
    url(r'host/detail/(?P<pk>[a-f\d]{8}(-[a-f\d]{4}){3}-[a-f\d]{12})/$', HostDetailView.as_view(template_name='assets/host_detail.html'), name='host-detail'),
    url(r'host/add/$', HostAddView.as_view(), name='host-add'),
    url(r'projects/$', ProjectsView.as_view(template_name='assets/projects_list.html'), name='projects-list'),
    url(r'project/(?P<pk>.*)/', ProjectDetailView.as_view(), name='project-detail'),
    url(r'projects/json/$', ProjectsJson.as_view(), name='projects-list-json'),
    url(r'projects/topo/$', ProjectTopologyView.as_view(template_name='assets/project_topo.html'), name='project-topo'),
    url(r'cluster/(?P<pk>.*)/', ClusterDetailView.as_view(), name='cluster-detail'),
    url(r'service/(?P<pk>.*)', ServiceDetailView.as_view(), name='service-detail'),
    url(r'hostsby/(?P<project>.*)/', HostsByProjectView.as_view(template_name='assets/hosts_list.html'), name='HostsbyProject')
    ] 