# Generated by Django 4.1.7 on 2023-02-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=2)),
                ('birth', models.CharField(default='19000101', max_length=8)),
                ('address', models.CharField(default='', max_length=100)),
                ('car_number', models.CharField(blank=True, max_length=20, null=True)),
                ('etc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
