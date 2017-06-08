# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_order', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderIn',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('isPay', models.BooleanField(default=False)),
                ('odata', models.DateTimeField(auto_now_add=True)),
                ('ototal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='df_user.FreshInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='df_order.OrderIn'),
        ),
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]
