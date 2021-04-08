# Generated by Django 3.1.7 on 2021-04-08 16:45

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello_mistri_app', '0023_auto_20210408_1645'),
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
        migrations.CreateModel(
            name='Clint_UID',
            fields=[
                ('clint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hello_mistri_app.clientinformation')),
                ('uid', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mistri_UID',
            fields=[
                ('mistri', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hello_mistri_app.mistriinformation')),
                ('uid', models.CharField(max_length=1000)),
            ],
        ),
    ]
