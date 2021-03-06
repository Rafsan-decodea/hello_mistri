# Generated by Django 3.1.7 on 2021-05-02 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0094_auto_20210502_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientinformation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mistriinformation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='service_name',
        ),
        migrations.RemoveField(
            model_name='subarea',
            name='area_name',
        ),
        migrations.RemoveField(
            model_name='subservice',
            name='service_name',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='ClientInformation',
        ),
        migrations.DeleteModel(
            name='MistriInformation',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceType',
        ),
        migrations.DeleteModel(
            name='SubArea',
        ),
        migrations.DeleteModel(
            name='SubService',
        ),
    ]
