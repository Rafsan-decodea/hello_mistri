# Generated by Django 3.1.7 on 2021-04-11 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0038_admin_clientinformation_clint_uid_mistri_uid_mistriinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='clint_uid',
            name='clint',
        ),
        migrations.RemoveField(
            model_name='mistri_uid',
            name='mistri',
        ),
        migrations.RemoveField(
            model_name='mistriinformation',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClientInformation',
        ),
        migrations.DeleteModel(
            name='Clint_UID',
        ),
        migrations.DeleteModel(
            name='Mistri_UID',
        ),
        migrations.DeleteModel(
            name='MistriInformation',
        ),
    ]
