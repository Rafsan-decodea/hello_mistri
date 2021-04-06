# Generated by Django 3.1.7 on 2021-04-06 07:26

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello_mistri_app', '0004_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
