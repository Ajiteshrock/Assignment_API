from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name="registration"),
    path('login/',views.LoginUser.as_view(),name='loginuser'),
    path('movies/add/',views.AddMovie.as_view(),name="Add_Movie"),
    path('movies/set_genre/',views.SetFavGenre,name='set_genre'),
    path('movies/',views.MoviesListView,name="movies_list"),
    path('movies/<int:pk>',views.MoviesDetailView,name="movies_details"),
    path('movies/vote/',views.VoteMovie.as_view(),name="movie_voting"),
    path('movies/review/',views.WriteMovieReview.as_view(),name="movie_reviewing"),
]   