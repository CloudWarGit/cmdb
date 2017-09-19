from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from assets.api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'hostType', views.HostTypeViewSet)
router.register(r'host', views.HostViewSet)
router.register(r'container', views.ContainerViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'cluster', views.ClusterViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'externalservice', views.ExternalServiceViewSet)


# hosttpye_detail = views.HostTypeViewSet.as_view({'get':'retrieve','post':'create'})

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]