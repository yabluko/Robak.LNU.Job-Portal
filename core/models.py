from django.db import models


class Users(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    job_title = models.TextField()


class Job(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    company_name = models.TextField()
    job_title = models.TextField()
    job_description = models.TextField()
    job_requirements = models.TextField()

class Posts(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateField()
