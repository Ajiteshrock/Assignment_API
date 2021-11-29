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
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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
    serializer_class = serializers.MovieAddSerializer

@swagger_auto_schema(methods=['post'] ,manual_parameters=None,request_body=serializers.GenreSerializer)
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


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def MoviesDetailView(request,pk):
        movie = models.Movie.objects.filter(id=pk)
        serializer = serializers.MovieSerializer(movie, many=True)
        return Response(serializer.data)

class VoteMovie(CreateAPIView):
    serializer_class = serializers.VoteSerializer
    permission_classes = [IsAuthenticated,]


class WriteMovieReview(CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated,]

"""
Public Views 
"""

@api_view(['GET'])
@permission_classes([AllowAny,])
def MoviesListView(request):
    query = request.query_params.get('sort_by',None)
    if query==None:
        movies = models.Movie.objects.all().order_by('-id')
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        movies = models.Movie.objects.all().order_by('-id')
        serializer = serializers.MovieSerializer(movies,many=True)
        upvotes = []
        response_dict_ = {}
        Response_data = {'Movie_Name and '+query:[]}
        visited={}
        for i in serializer.data:
            i = dict(i)
            for j in i:
                if i['name'] not in visited:
                    visited[i['name']]=1
                    Response_data['Movie_Name and '+query].append((i['name'],i['votes_'][query]))   
        
        def sort_by_votes(tup): 
            lst = len(tup) 
            for i in range(0, lst): 
                for j in range(0, lst-i-1): 
                    if (tup[j][1] > tup[j + 1][1]): 
                        temp = tup[j] 
                        tup[j]= tup[j + 1] 
                        tup[j + 1]= temp 
            return tup  
        Response_data = sort_by_votes(Response_data['Movie_Name and '+query])
        return Response(Response_data)

    


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetRecommendationAPI(request):
    id = request.user.id
    user_model = models.ProfileUser.objects.get(user_id=id)
    genre = user_model.fav_genre
    genre = models.Genre.objects.get(genre=genre)
    recommeded_movies = models.Movie.objects.filter(genre=genre)
    serializer = serializers.MovieSerializer(recommeded_movies,many=True)
    return Response(serializer.data)
