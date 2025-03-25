from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer

from .models import Movie

RELEASE_DATE_LIMIT = 1900
RESUME_CHARACTERS = 500


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < RELEASE_DATE_LIMIT:
            raise serializers.ValidationError("Release date cannot be before 1900")
        return value

    def validade_resume(self, value):
        if len(value) > RESUME_CHARACTERS:
            raise serializers.ValidationError(
                "Resume must not be longer than 500 characters"
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]

        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
