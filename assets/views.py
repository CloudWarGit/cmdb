from django.shortcuts import render, get_object_or_404
from assets.models import *

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

from django.utils import timezone
from django.http.response import JsonResponse

from utils.treeview import TreeNode, get_project_tree

class AssetsView(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')


class HostsView(ListView):
    model = Host
    object_list = Host.objects.order_by('create_time')
    def get_context_data(self, **kwargs):
        context = super(HostsView, self).get_context_data(**kwargs)
        context['create_time'] = timezone.now()
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, 'assets/hosts_list.html', context=self.get_context_data())
    
class HostDetailView(DetailView): 
    model = Host   
    
class HostAddView(CreateView):
    model = Host
    fields = ['name', 'type', 'inner_ip', 'out_ip', 'os', 
              'project', 'status', 'create_time', 
              'total_up_time','cost','custom_tag','summary']

class ProjectsJson(ListView):
    model = Project
    def get(self, request, *args, **kwargs):
        root = Project.objects.all()
        data = get_project_tree(root)
        return JsonResponse(data, safe=False)
    
class ProjectsView(ListView):
    model = Project
    
class ProjectDetailView(DetailView):
    model = Project
    
class HostsByProjectView(ListView):
    def get_queryset(self):
        self.project = get_object_or_404(Project, name=self.kwargs['project'])
        return Host.objects.filter(project=self.project)
     
    def get_context_data(self, **kwargs):
        context = super(HostsByProjectView, self).get_context_data(**kwargs)
        context['Project'] = self.project
        return context
    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'assets/hosts_list.html', context=self.get_context_data())
    
class ProjectTopologyView(ListView): 
    model = Project
    
class ClusterView(ListView):
    model = Cluster
    
class ClusterDetailView(DetailView):
    model = Cluster

class ServicesView(ListView):
    model = Service
    
class ServiceDetailView(DetailView):
    model = Service