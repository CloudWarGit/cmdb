from django.contrib import admin
from assets.models import *
# Register your models here.

for model in [Host, HostType, Project, Service, Container, ExternalService, Cluster] :
    admin.site.register(model)
    
