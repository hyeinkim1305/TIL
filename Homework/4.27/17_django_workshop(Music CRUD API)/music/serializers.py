from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name',)          # id는 자동?

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    
    class Meta:
        model = Artist
        fields = '__all__'

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title',)