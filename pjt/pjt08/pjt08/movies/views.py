from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie, Review, Comment
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, CommentListSerializer


@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete' : f'{review_pk}글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
