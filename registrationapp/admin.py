from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile , Post, Vacancy, Company, CompanyProfile

# Register your models here.
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class CompanyProfileInline(admin.StackedInline):
    model = CompanyProfile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [
        ProfileInline
    ]

    
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    # fields = ["name"]
    inlines = [
        CompanyProfileInline
    ]


# Unregister initial User
admin.site.unregister(User)    

# Register of User and Profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile) 

admin.site.register(Post)


admin.site.register(Vacancy)

admin.site.register(Company, CompanyAdmin)