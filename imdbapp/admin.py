from django.contrib import admin
from imdbapp.models import (Movie, Director, Genre)
admin.site.site_title = "IMDB"
admin.site.site_header = "IMDB"


class AdminMovie(admin.ModelAdmin):
    list_filter = ('inactive',)
    list_display = ('name', 'popularity', 'director', 'imdb_score', 'inactive')
    list_display_links = ('name',)


admin.site.register(Movie, AdminMovie)
admin.site.register(Director)
admin.site.register(Genre)
