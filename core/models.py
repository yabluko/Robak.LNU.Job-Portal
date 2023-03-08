from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.user.username

