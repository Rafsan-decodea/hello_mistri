# Generated by Django 3.1.7 on 2021-04-07 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0011_clientinformation_mistriinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientInformation',
        ),
        migrations.DeleteModel(
            name='MistriInformation',
        ),
    ]
