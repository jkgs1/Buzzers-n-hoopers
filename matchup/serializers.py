from matchup.models import *
from rest_framework import serializers

class MatchSerializer(serializers.ModelSerializer):
    full_title = serializers.CharField(source='printer', read_only=True)
    class Meta:
        model = Match
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class MatchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields = '__all__'

class MatchAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchAdmin
        fields = '__all__'
