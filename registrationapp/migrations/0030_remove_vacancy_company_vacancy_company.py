# Generated by Django 4.1.7 on 2023-06-01 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0029_vacancy_bio_vacancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_of_company', to='registrationapp.company'),
        ),
    ]
