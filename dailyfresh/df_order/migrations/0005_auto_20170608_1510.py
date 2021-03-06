# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
        ('df_order', '0004_auto_20170608_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('isPay', models.BooleanField(default=False)),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('ototal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='df_user.FreshInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetailin',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='orderdetailin',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderin',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderDetailIn',
        ),
        migrations.DeleteModel(
            name='OrderIn',
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='df_order.OrderInfo'),
        ),
    ]
