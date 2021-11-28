### API(IMDB Clone)

### Set-Up
## Please install latest version of PIP from [here](https://pypi.org/project/pip/)

### pip install requirements..txt
### Git clone - The URL 
### Create Superuser - python manage.py craetesuperuser
### Go to Assignment_API and run python manage.py runserver

## End-Points

### admin/ - For administration login
### demoapi/register - For Registration
### demoapi/login - For Login (Token Based Authenticaton)
### demoapi/movies/ - Public API (No need to authentication) Showing all Movie List
### demoapi/movies/id - Showing Particular Movie Detail ( Auth required)
### demoapi/movies/vote - Upvoting/Downvoting for a Movie
### demoapi/movies/review - Writing a review for a movie
### demoapi/movies/set_genre - Setting Favourite Genre
### demoapi/movies/add - Adding Movie in movie_database

## Pending API
### demoapi/movies/?sort_by - Sorting bases on upvoting or downvoting
### Reverse Relation Represtation for Votes and Reviews
### Deployment On Heroku.