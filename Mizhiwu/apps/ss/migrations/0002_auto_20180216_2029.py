# Generated by Django 2.0.1 on 2018-02-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='show',
            field=models.IntegerField(choices=[(1, '显示'), (0, '不显示')], default=1, verbose_name='是否显示'),
        ),
    ]
