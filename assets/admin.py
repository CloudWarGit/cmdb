from django.contrib import admin
from assets.models import *
# Register your models here.

for model in [Host, Service, Container, ExternalService, HostType, Project, Cluster, Group] :
    admin.site.register(model)
    
