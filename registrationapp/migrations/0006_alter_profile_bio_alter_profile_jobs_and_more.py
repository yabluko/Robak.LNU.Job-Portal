# Generated by Django 4.1.7 on 2023-05-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0005_profile_profile_imgae'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
