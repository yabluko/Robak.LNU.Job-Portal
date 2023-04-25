from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup , name="signup"),
    path('profile_list', views.profile_list, name="profile_list"),
    path('', views.home, name="home" ),
]