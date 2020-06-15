# Generated by Django 3.0.3 on 2020-06-15 11:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dgsys2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='estimated_end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='equipmentprice',
            name='equipment_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='dgsys2.Equipment'),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='itempurchase',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='dgsys2.ItemPrice', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
