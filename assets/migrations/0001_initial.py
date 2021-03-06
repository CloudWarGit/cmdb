# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-13 03:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='集群名称')),
                ('environment', models.CharField(choices=[('正式', '正式'), ('预发布', '预发布'), ('测试', '测试')], max_length=100, verbose_name='环境类型')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='HostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('物理机', '物理机'), ('ec2', 'ec2'), ('bcc', 'bcc'), ('aliyun', 'aliyun'), ('ucloud', 'ucloud')], max_length=50, verbose_name='主机类型')),
                ('configinfo', models.CharField(blank=True, max_length=100, verbose_name='配置信息')),
                ('region', models.CharField(blank=True, choices=[('cn-north-1', 'cn-north-1'), ('cn-north-1a', 'cn-north-1a'), ('华北', '华北'), ('办公区二层', '办公区二层'), ('办公区四层', '办公区四层')], max_length=100, null=True, verbose_name='区域')),
                ('price', models.FloatField(verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(default='果壳', max_length=100, primary_key=True, serialize=False, verbose_name='项目名称')),
                ('company', models.CharField(blank=True, max_length=100, verbose_name='所属')),
                ('lifecycle', models.CharField(choices=[('测试中', '测试中'), ('已上线', '已上线'), ('停运', '停运')], max_length=100, verbose_name='生命周期')),
                ('owner', models.CharField(blank=True, max_length=32, verbose_name='负责人')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.Asset')),
            ],
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.Asset')),
                ('name', models.CharField(max_length=100, verbose_name='容器名称')),
                ('image', models.CharField(max_length=100, verbose_name='镜像名称')),
                ('status', models.CharField(max_length=100, verbose_name='状态')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('slug', models.SlugField()),
            ],
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='ExternalService',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.Asset')),
                ('name', models.CharField(max_length=100, verbose_name='服务名称')),
                ('vendor', models.CharField(max_length=100, verbose_name='服务商')),
                ('api', models.URLField()),
                ('price', models.FloatField(verbose_name='价格')),
                ('cost', models.FloatField(verbose_name='已消费')),
                ('slug', models.SlugField()),
            ],
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.Asset')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='主机名')),
                ('inner_ip', models.GenericIPAddressField(verbose_name='内网ip')),
                ('out_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='外网ip')),
                ('os', models.CharField(blank=True, max_length=32, verbose_name='操作系统')),
                ('status', models.IntegerField(choices=[(0, '运行中'), (1, '停止'), (2, '已销毁')], verbose_name='运行状态')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('total_up_time', models.TimeField(verbose_name='累计运行时')),
                ('cost', models.FloatField(verbose_name='成本')),
                ('custom_tag', django.contrib.postgres.fields.jsonb.JSONField(blank=True, max_length=100, null=True, verbose_name='自定义标签')),
                ('summary', models.TextField(blank=True, max_length=500, verbose_name='描述')),
                ('slug', models.SlugField()),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Project', verbose_name='所属业务')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.HostType')),
            ],
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.Asset')),
                ('name', models.CharField(max_length=100, verbose_name='服务名称')),
                ('ip', models.GenericIPAddressField(verbose_name='应用ip')),
                ('port', models.PositiveIntegerField(blank=True, verbose_name='端口号')),
                ('version', models.CharField(blank=True, max_length=32, verbose_name='版本')),
                ('slug', models.SlugField()),
            ],
            bases=('assets.asset',),
        ),
        migrations.AddField(
            model_name='cluster',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='assets.Project', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='service',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='assets.Cluster', verbose_name='所属集群'),
        ),
        migrations.AddField(
            model_name='service',
            name='host',
            field=models.ManyToManyField(related_name='children', to='assets.Host', verbose_name='所在主机'),
        ),
    ]
