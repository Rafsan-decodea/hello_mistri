# Generated by Django 3.1.7 on 2021-06-16 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello_mistri_app', '0111_auto_20210616_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
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
            name='SubArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_area_name', models.CharField(max_length=100)),
                ('area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.area')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('service_type_rate', models.CharField(max_length=100)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.subservice')),
            ],
        ),
        migrations.CreateModel(
            name='OrderSubmitByClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_holder_name', models.CharField(max_length=100)),
                ('order_holder_pic', models.CharField(max_length=500)),
                ('order_holder_city', models.CharField(max_length=500)),
                ('order_holder_area', models.CharField(max_length=500)),
                ('service_name', models.CharField(max_length=100)),
                ('sub_service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(max_length=100)),
                ('service_type_rate', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MistriInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mistri_id', models.CharField(max_length=10)),
                ('uid', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=100)),
                ('profile_image_link', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('image', models.ImageField(upload_to='media')),
                ('dob', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=200)),
                ('sub_area', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('ability', models.CharField(max_length=100, null=True)),
                ('expiriance', models.CharField(max_length=200, null=True)),
                ('emargency', models.CharField(max_length=100)),
                ('emargency_name', models.CharField(max_length=200)),
                ('emargency_number', phone_field.models.PhoneField(help_text='emargency_contuct', max_length=31)),
                ('education', models.CharField(max_length=200)),
                ('is_bick', models.CharField(max_length=20)),
                ('is_instrument', models.CharField(max_length=20)),
                ('helper_mistri', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=200)),
                ('sub_service', models.CharField(max_length=200)),
                ('service_type', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clint_id', models.CharField(max_length=10)),
                ('uid', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=100)),
                ('profile_image_link', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=200)),
                ('sub_area', models.CharField(max_length=200)),
                ('home_address', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_mistri_app.city'),
        ),
    ]
