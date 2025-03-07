from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin

from clubber.models import *


class PlayerSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def get_permissions_map(self, created: bool):
        p: Player = self.instance
        if p.user:
            return {
                'view_player': [p.user],
                'change_player': [p.user],
                'delete_player': [p.user]
            }
        else:
            current_user = self.context['request'].user
            return {
                'view_player': [current_user],
                'change_player': [current_user],
                'delete_player': [current_user]
            }

class TeamPlayerSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = TeamPlayer
        fields = '__all__'

    def get_permissions_map(self, created: bool):
        tp: TeamPlayer = self.instance
        if tp.team.club is None:
            current_user = self.context['request'].user
            return {
                'view_team': [current_user],
                'change_team': [current_user],
                'delete_team': [current_user],
            }
        else:
            return {
                'view_team_player': [tp.team.club.aclGroup],
                'change_team_player': [tp.team.club.aclGroup],
                'delete_team_player': [tp.team.club.aclGroup]
            }

class TeamSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


    def get_permissions_map(self, created: bool):
        t: Team = self.instance
        if t.club is None:
            current_user = self.context['request'].user
            return {
                'view_team': [current_user],
                'change_team': [current_user],
                'delete_team': [current_user],
            }
        else:
            return {
                'view_team': [t.club.aclGroup],
                'change_team': [t.club.aclGroup],
                'delete_team': [t.club.aclGroup]
            }



class ShirtSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = '__all__'


class ClubSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

    def get_permissions_map(self, created: bool):
        c: Club = self.instance
        if c.aclGroup is None:
            g: Group = Group(name=f'team-{c.name}')
            g.save()
            g.refresh_from_db()
            current_user: User = self.context['request'].user
            current_user.groups.add(g)
            c.aclGroup = g
            c.save()

            return {
                'view_club': [g],
                'change_club': [g],
                'delete_club': [g]
            }
        else:
            return {
                'view_club': [c.aclGroup],
                'change_club': [c.aclGroup],
                'delete_club': [c.aclGroup]
            }
