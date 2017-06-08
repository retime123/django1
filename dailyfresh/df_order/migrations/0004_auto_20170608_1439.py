# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
        ('df_order', '0003_auto_20170608_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
                ('order', models.ForeignKey(to='df_order.OrderIn')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetailinfo',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='orderdetailinfo',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderDetailInfo',
        ),
    ]
