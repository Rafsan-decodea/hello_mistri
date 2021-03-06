# Generated by Django 3.1.7 on 2021-04-07 16:54

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello_mistri_app', '0014_auto_20210407_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clint_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MistriInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mistri_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('image', models.ImageField(upload_to='media')),
                ('dob', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
