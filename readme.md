### API(IMDB Clone)

### For Live preview of the APP
### Deployed on Heroku 
### [Here](https://imdbcloneapi1.herokuapp.com)
### [Documentation|Swagger UI](https://imdbcloneapi1.herokuapp.com/documentation/)
### [POSTMAN Collections](https://github.com/Ajiteshrock/Assignment_API/tree/master/postman)

### Set-Up
## Please install latest version of PIP from [here](https://pypi.org/project/pip/)

### pip install requirements..txt
### Git clone - The URL 
### Create Superuser - python manage.py craetesuperuser
### Go to Assignment_API and run python manage.py runserver

## End-Points

## Public APIs
### demoapi/movies/ - Public API (No need to authentication) Showing all Movie List
### demoapi/movies/?sort_by=Upvote - Sorting bases on upvoting 
### demoapi/movies/?sort_by=Downvotes - Sorting bases on downvoting

## Private APIs (Login Required)
### documentation/ - For Whole Documentation
### admin/ - For administration login
### demoapi/register - For Registration
### demoapi/login - For Login (Token Based Authenticaton ( JWT Token))
### demoapi/movies/id - Showing Particular Movie Detail ( Auth required)
### demoapi/movies/vote - Upvoting/Downvoting for a Movie
### demoapi/movies/review - Writing a review for a movie
### demoapi/movies/set_genre - Setting Favourite Genre
### demoapi/movies/add - Adding Movie in movie_database
### demoapi/movies/getrecommendation - Getting Recommendation according to Fav Genre .

