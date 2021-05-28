# Generated by Django 3.1.7 on 2021-05-28 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello_mistri_app', '0099_remove_clientinformation_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSubmitByClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('sub_service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
