# Generated by Django 3.1.7 on 2021-04-25 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0072_city_clientinformation_mistriinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.RemoveField(
            model_name='mistriinformation',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClientInformation',
        ),
        migrations.DeleteModel(
            name='MistriInformation',
        ),
    ]
