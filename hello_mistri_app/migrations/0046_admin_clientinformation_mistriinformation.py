# Generated by Django 3.1.7 on 2021-04-11 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello_mistri_app', '0045_auto_20210411_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clint_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MistriInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mistri_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('image', models.ImageField(upload_to='media')),
                ('dob', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.clientinformation')),
            ],
        ),
    ]
