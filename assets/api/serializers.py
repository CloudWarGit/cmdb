from rest_framework import serializers
from assets.models import *

class HostTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='assets-api:hosttype-detail', format='html')
    class Meta:
        model = HostType
        fields = ('url','type','configinfo','region','price')
        
class HostSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedRelatedField(queryset=HostType.objects.all(), view_name='assets-api:hosttype-detail')
    class Meta:
        model = Host
        fields = ('url','name','type','inner_ip','out_ip','os',
                  'project','group','status','create_time',
                  'total_up_time','cost','custom_tag','summary')
        
# class HostSerializer(serializers.ModelSerializer):
# #     type = serializers.HyperlinkedRelatedField(queryset=HostType.objects.all(), view_name='assets-api:hosttype-detail')
#     class Meta:
#         model = Host
#         fields = ('url','name','type','inner_ip','out_ip','os',
#                   'project','group','status','create_time',
#                   'total_up_time','cost','custom_tag','summary')
        
class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = ('name','image','status','create_time')
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('name','children_groups','vars')
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name','company', 'lifecycle','owner')
        
class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cluster
        fields = ('name','environment','project')
        
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'ip', 'port', 'cluster', 'host')
        
class ExternalServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalService
        fields = ('name','vendor','api','price','cost')