from django.shortcuts import render
from . import serializers
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.generics import RetrieveAPIView , ListAPIView , CreateAPIView , ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
# from .serializers import MyTokenObtainPairSerializerStudent, StudentSerializser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from . import models
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_object_or_404

  
#Registration View
class RegisterUser(CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = dict(serializer.data)
        print(response_data)
        response_data['message']='You are registered'
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


#Login View   


class LoginUser(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.MyTokenObtainPairSerializerUser

#Movie Serializers

class AddMovie(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.MovieSerializer

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated,])
def SetFavGenre(request):
    if request.method == "POST":
        data = request.data
        request.data['user'] = request.user.id
        user = models.ProfileUser.objects.get(user_id=request.data['user'])
        Genre = models.Genre.objects.get(genre=request.data['Genre'])
        user.fav_genre = Genre
        user.save()
        return Response({"message":"Your Favourtie genre is all set"})
    all_genres = models.Genre.objects.all()
    l=[]
    for i in all_genres:
        l.append(i.genre)
    return Response({'All Genres':l})
      
class MoviesDetail(RetrieveAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()
    permission_classes = [IsAuthenticated,]

class VoteMovie(CreateAPIView):
    serializer_class = serializers.VoteSerializer
    permission_classes = [IsAuthenticated,]


class WriteMovieReview(CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated,]

"""
Public Views 
"""

class MoviesListView(ListAPIView):
    serializer_class = serializers.MovieSerializer
    permission_classes = [AllowAny,]
    queryset = models.Movie.objects.all()

   