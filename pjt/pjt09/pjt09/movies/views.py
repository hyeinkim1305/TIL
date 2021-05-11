from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Genre
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request):
    genres = Genre.objects.all()
    context = {
        'genres' : genres,
    }
    return render(request, 'movies/recommended.html', context)

def genre_recommended(request, genre_pk):
    if request.user.is_authenticated:
        genre = get_object_or_404(Genre, pk=genre_pk)
        movies = genre.movie_set.all()
        # movies = serializers.serialize("json", movies)
        context = {
            'movies' : movies
        }
        return JsonResponse(context)
    return HttpResponse(status=401)
