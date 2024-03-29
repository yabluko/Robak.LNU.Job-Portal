from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('signup', views.signup , name="signup"),
    path('profile_list', views.profile_list, name="profile_list"),
    path('', views.main, name="main" ),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home', views.home, name="home"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path('logout', views.logout_user, name="logout"),
    path('update_user', views.update_user, name='update_user'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('vacancies/creation', views.vacancies__creating, name='vacancies_creation'),
    path('post_likes/<int:pk>', views.post_likes , name="post_likes" ),
    path('vacancies/recommended/<int:vacancy_pk>', views.vacancies_recommended, name='vacancies_recommended'),
    path('favourites/<int:id>', views.favourites, name='favourite_add'),
    path('favourites/list', views.favourites_list, name='favourite_list'),
    path('vacancies/searched_vacancies/', views.searched_vacancies, name='searched_vacancies'),
    path('vacancies/searched_vacancies_bio/<int:vacancy_pk>/', views.searched_vacancies_bio, name='searched_vacancies_bio'),
    path('events_list/', views.events_list, name='events_list'),
    path('people/', views.people_list, name='people_list'),
]