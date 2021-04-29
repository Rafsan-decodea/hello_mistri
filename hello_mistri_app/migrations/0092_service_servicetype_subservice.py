# Generated by Django 3.1.7 on 2021-04-29 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_mistri_app', '0091_auto_20210428_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_service_name', models.CharField(max_length=100)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.subservice')),
            ],
        ),
    ]