# Generated by Django 4.1.7 on 2023-06-01 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0024_companyprofile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
    ]
