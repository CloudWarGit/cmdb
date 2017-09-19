# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20170713_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='主机组')),
                ('vars', models.CharField(blank=True, max_length=100, null=True, verbose_name='组变量')),
                ('host', models.ManyToManyField(blank=True, to='assets.Host', verbose_name='包含主机')),
                ('parent_group', models.ManyToManyField(blank=True, to='assets.Group', verbose_name='依赖服务')),
            ],
        ),
    ]
