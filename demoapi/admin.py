from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Votes)
admin.site.register(models.Genre)
admin.site.register(models.ProfileUser)
admin.site.register(models.Review)