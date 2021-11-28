from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Genre(models.Model):

    genre = models.CharField(max_length=60)
    def __str__(self):
        return self.genre 

class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fav_genre = models.ForeignKey(Genre,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.user.username
#signal when a user gets created the same user created here
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profileuser.save()


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
   
    def __str__(self):
        return self.name

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upvote = models.BooleanField()
    downvote = models.BooleanField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.review
