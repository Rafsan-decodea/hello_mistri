# Generated by Django 3.1.7 on 2021-04-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0042_admin_clientinformation_mistriinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
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
