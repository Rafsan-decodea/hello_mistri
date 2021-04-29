# Generated by Django 3.1.7 on 2021-04-27 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0085_area_city_clientinformation_mistriinformation_service_subservice'),
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
            name='SubService',
        ),
    ]