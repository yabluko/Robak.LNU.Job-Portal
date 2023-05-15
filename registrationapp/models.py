from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms

# Create your models here.


class Post(models.Model):
    user =  models.ForeignKey(
        User, related_name="meeps",
        on_delete=models.DO_NOTHING
        )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.user}"
            f"({self.created_at: %Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
            related_name="followed_by",
            symmetrical=False,     
            blank=True
            )
    first_name = models.CharField(max_length=200,null=True, blank=True)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    username = models.CharField(max_length=200,null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    jobs = models.CharField(max_length=200,null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)
    skills = models.CharField(max_length=200,null=True, blank=True)
    
    def followers_count(self):
        return self.follows.count()

    def __str__(self):
        return self.user.username 


# Create automatical profile for user 
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)