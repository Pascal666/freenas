# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-26 18:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0005_auto_20171025_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='memory',
            field=models.IntegerField(help_text='Megabytes of RAM for the virtual machine.This memory will be allocated when the VM is running and not available to the host system or other VMs.', validators=[django.core.validators.MinValueValidator(256)], verbose_name='Memory Size (MiB)'),
        ),
    ]
