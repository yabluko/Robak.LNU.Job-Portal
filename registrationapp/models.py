from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django import forms
from ckeditor.fields import RichTextField

# Create your models here.

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

    def count_followers(self):
        followers = self.followed_by.all()
        return followers.count()


    def __str__(self):
        return self.user.username 
    

class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    employee = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.name
    

class CompanyProfile(models.Model):
    company = models.OneToOneField(Company,on_delete=models.CASCADE, null=True, blank=False)
    follows = models.ManyToManyField(User,
            related_name="followed_companies",
            symmetrical=False,     
            blank=True
            )
    company_referral = models.CharField(max_length=200, null=True,blank=False)
    company_location = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self) -> str:
        return self.company.name


class Vacancy(models.Model):
    company = models.ForeignKey(Company, related_name="vacancy_of_company",null=True, blank=False,  on_delete=models.CASCADE)
    position = models.CharField(max_length=200,null=True, blank=False)     
    type_of_workplace = models.CharField(max_length=200,null=True, blank=False)     
    vacancy_region = models.CharField(max_length=200,null=True, blank=False)     
    type_of_employment = models.CharField(max_length=200,null=True, blank=False)      
    bio_vacancy = RichTextField(blank=True, null=True)
    date_created = models.DateField(auto_now=True)
    skills = models.CharField(max_length=200,null=True, blank=False)
    favourites = models.ManyToManyField(User, related_name='favourite',default=None, blank=True)


    def __str__(self):              
        return f"{self.company.name} - {self.position}"
    
class Event(models.Model):
    event_id = models.CharField(max_length=200, null=True, blank=True)
    event_type = models.CharField(max_length=200, null=True, blank=True)    
    event_img = models.ImageField(null=True, blank=True, upload_to="images/")
    event_name = models.CharField(max_length=200, null=True, blank=True)
    event_datatime = models.CharField(max_length=200, null=True, blank=True)
    event_url = models.CharField(max_length=200, null=True, blank=True)


class Post(models.Model):
    user =  models.ForeignKey(
        User, related_name="posts_user",
        on_delete=models.CASCADE
        )
    company = models.ForeignKey(
        Company, related_name="posts_company",
        on_delete=models.CASCADE, null=True, blank=True
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)


    def likes_count(self):
        return self.likes.count()

    def __str__(self) -> str:
        return (
            f"{self.user}"
            f"({self.created_at: %Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )

# Create automatical profile for user
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)


def create_profile_of_company(sender, instance, created, **kwargs):
    if created:
        company_profile = CompanyProfile(company=instance)
        company_profile.save()

post_save.connect(create_profile_of_company, sender=Company)        