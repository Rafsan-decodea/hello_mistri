# Generated by Django 3.1.7 on 2021-04-22 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0065_clientinformation_mistriinformation'),
    ]

    operations = [
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