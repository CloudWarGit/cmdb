# -*- coding: utf-8 -*-

from django.db import models
import uuid
from django.urls import reverse
from django.contrib.postgres.fields.jsonb import JSONField

# Create your models here.

REGION = (
    (i,i) for i in 
    ("cn-north-1",
     "cn-north-1a",
     "华北",
     "办公区二层",
     "办公区四层")
    )

ENVIRONMENT = (
    (i,i) for i in 
    ("正式",
     "预发布",
     "测试")
    )

class Asset(models.Model):
    asset_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)

class HostType(models.Model):
    HOST_TYPE = (
        (i,i) for i in
        ("物理机",
        "ec2",
        "bcc",
        "aliyun",
        "ucloud")
        )
    type = models.CharField("主机类型", max_length=50, choices=HOST_TYPE)
    configinfo = models.CharField("配置信息", max_length=100, blank=True)
    region = models.CharField("区域", max_length=100,choices=REGION, blank=True, null=True)
    price = models.FloatField("价格")
     
    def __str__(self):
        verbose_name = self.type + " | " + self.configinfo 
        return verbose_name

class Host(Asset):
    HOST_STATUS = (
        (0, "运行中"),
        (1, "停止"),
        (2, "已销毁")
        )
    
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("主机名", max_length=100, blank=True)
    type = models.ForeignKey(HostType,on_delete=models.CASCADE)
    inner_ip = models.GenericIPAddressField("内网ip")
    out_ip = models.GenericIPAddressField("外网ip", blank=True, null=True)
    os = models.CharField("操作系统", max_length=32, blank=True)
    project = models.ForeignKey('Project', verbose_name='所属业务', blank=True, null=True)
#     service = models.ManyToManyField('Service', verbose_name='运行服务', blank=True)
    status = models.IntegerField("运行状态", choices=HOST_STATUS)
    create_time = models.DateTimeField(verbose_name="创建时间")
    total_up_time = models.TimeField("累计运行时")
    cost = models.FloatField("成本")
    custom_tag = JSONField("自定义标签", max_length=100,blank=True, null=True)
    summary = models.TextField("描述", max_length=500, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('host-detail', kwargs={'pk':self.pk})

class Container(Asset):
    name = models.CharField("容器名称", max_length=100)
    image = models.CharField("镜像名称", max_length=100)
    status = models.CharField("状态", max_length=100)
    create_time = models.DateTimeField(verbose_name="创建时间")

class Project(models.Model):
    LIFE_CYCLE = (
        (i, i) for i in 
        ("测试中",
         "已上线",
         "停运")
        )
    name = models.CharField("项目名称", default='果壳', max_length=100, primary_key=True)
    company = models.CharField("所属", max_length=100, blank=True)
    lifecycle = models.CharField("生命周期", max_length=100, choices=LIFE_CYCLE)
#     version = models.CharField("版本号", max_length=32, blank=True)
    owner = models.CharField("负责人", max_length=32, blank=True)
    
    def __str__(self):
        return self.name

class Cluster(models.Model):
    name = models.CharField("集群名称", max_length=100)
    environment = models.CharField("环境类型", max_length=100, choices=ENVIRONMENT)
    project = models.ForeignKey(Project, verbose_name = '所属项目', related_name="children")
    
    def __str__(self):
        return self.name

class Service(Asset):
    name = models.CharField("服务名称", max_length=100)
    ip = models.GenericIPAddressField("应用ip")
    port = models.PositiveIntegerField("端口号", blank=True)
    cluster = models.ForeignKey(Cluster, verbose_name = '所属集群', related_name="children")
    host = models.ManyToManyField(Host, verbose_name = '所在主机', related_name="children")
    #     parent_service = models.ForeignKey("self", verbose_name = "父服务", related_name="children", blank=True, null=True)
    #     depend_services = models.ManyToManyField("self", verbose_name='依赖服务', symmetrical=False, blank=True, null=True)
    version = models.CharField("版本", max_length=32, blank=True)
      
    def __str__(self):
        return self.name
#         return self.project.name + "." +self.name
    
class ExternalService(Asset):
    name = models.CharField("服务名称", max_length=100)
    vendor = models.CharField("服务商", max_length=100)
    api = models.URLField()
    price = models.FloatField("价格")
    cost = models.FloatField("已消费")
    

class Configuration(Asset):
    pass

class Relationship(models.Model):
    pass