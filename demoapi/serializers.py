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
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Votes
        fields = "__all__"
        


class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Review
        fields = "__all__"

    
       
  
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileUser
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source="genre.genre")
    allreviews = serializers.SerializerMethodField('reviews')
    votes_ = serializers.SerializerMethodField('votes')
    class Meta:    
        model = models.Movie
        fields = ('name','release_date','genre','allreviews','votes_')
    
    def reviews(self,obj):
        reviews = obj.review_movie.all()
        l=[{'Review and Written By':[]}]
        for i in reviews:
            l[0]["Review and Written By"].append((i.review+" ",i.user.username))
            
        return l
    def votes(self,obj):
        votes_ = obj.movie_votes.all()
        l = {'Upvote':0,
             'Downvotes':0}
        for i in votes_:
            if i.upvote:
                l['Upvote']+=1
            elif i.downvote:
                l['Downvotes']+=1
        return l