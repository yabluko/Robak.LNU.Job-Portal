# Generated by Django 4.1.7 on 2023-06-01 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0022_delete_orderedpost_vacancy_company_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_referral', models.CharField(max_length=200, null=True)),
                ('company_location', models.CharField(max_length=200, null=True)),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_of_company', to='registrationapp.company')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_company', to='registrationapp.company'),
        ),
    ]
