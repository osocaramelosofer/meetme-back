from rest_framework import serializers
from ..models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'day_or_night', 'favorite_day', 'favorite_color')
        model = Quiz
