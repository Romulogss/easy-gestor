# Generated by Django 3.2.5 on 2021-07-16 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210713_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='valor',
        ),
        migrations.AddField(
            model_name='servicoprestado',
            name='descricao',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicoprestado',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicoprestado',
            name='data',
            field=models.DateField(default=datetime.date(2021, 7, 16)),
        ),
    ]