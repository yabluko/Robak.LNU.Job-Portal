from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
      first_name = models.CharField('User name', max_length=30)
      last_name = models.CharField('User last name', max_length=30)
      username = models.CharField('Username', max_length=30)
      email = models.CharField('User email', max_length=30 , blank=False)
      password = models.CharField('User password', max_length=30,  blank=False )


def __str__(self):
    return self.first_name
