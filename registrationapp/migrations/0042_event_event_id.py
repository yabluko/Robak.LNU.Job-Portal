# Generated by Django 4.1.7 on 2023-06-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0041_rename_data_event_event_event_datatime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
