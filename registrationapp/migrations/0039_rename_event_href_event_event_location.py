# Generated by Django 4.1.7 on 2023-06-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0038_event_event_data_event_event_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_href',
            new_name='event_location',
        ),
    ]
