from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from . import models

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {'password': {'write_only': True}} #can not see hashable password
    
    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

      
class MyTokenObtainPairSerializerUser(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializerUser, cls).get_token(user)
        token['username'] = user.username
        return token
    
    def validate(self,attrs):
        data = super(MyTokenObtainPairSerializerUser, self).validate(attrs)
        data['message'] = 'Welcome Again'
        return data  



class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        exclude = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Votes
        #fields = "__all__"
        exclude = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Review
        exclude="id"
       

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileUser
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source="genre.genre")
    class Meta:  
        model = models.Movie
        fields = ('name','release_date','genre','movie_review','movie_votes')

