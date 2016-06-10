from django.contrib import admin

# Register your models here.
from movieratings_app.models import Rater, Movie, Rating

admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Rater)