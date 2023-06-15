from rest_framework import serializers
from registrationapp.models import Vacancy 


class VacancyModel:
    def __init__(self,company ,position ) :
        self.company = company
        self.position = position

class VacancySerializer(serializers.ModelSerializer):
    company = serializers.CharField(max_length=255)
    position = serializers.CharField()



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = { 
#             'username', 'first_name',
#         }