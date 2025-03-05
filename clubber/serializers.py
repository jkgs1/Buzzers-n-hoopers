from django.contrib.auth.models import Group
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin

from clubber.models import *
from rest_framework import serializers

class PlayerSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user

        return {
            'view_player': [True],
            'change_player': [current_user],
            'delete_player': [current_user]
        }

class TeamPlayerSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = TeamPlayer
        fields = '__all__'

class TeamSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ShirtSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = '__all__'

class ClubSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'