from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets,generics
from rest_framework.decorators import detail_route

from assets.models import *
from .serializers import *

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'hosts': reverse('host-list', request=request, format=format)
#     })

class HostTypeViewSet(viewsets.ModelViewSet):
    queryset = HostType.objects.all()
    serializer_class = HostTypeSerializer
    
#     @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
#     def highlight(self, request, *args, **kwargs):
#         hosttypes = self.get_object()
#         return Response(repr(hosttypes))
  
    def perform_create(self, serializer):
        serializer.save()
        
class HostViewSet(viewsets.ModelViewSet):        
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ExternalServiceViewSet(viewsets.ModelViewSet):
    queryset = ExternalService.objects.all()
    serializer_class = ExternalServiceSerializer