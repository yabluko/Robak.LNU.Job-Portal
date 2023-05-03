from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup , name="signup"),
    path('profile_list', views.profile_list, name="profile_list"),
    path('', views.main, name="main" ),
    path('home1', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name="profile"),
]