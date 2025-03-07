from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from common.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'user_permissions')

    def get_permissions_map(self, created: bool):
        u: User = self.instance
        g = Group.objects.get_or_create(name='users')
        u.groups.add(g)

        return {
            'view_user': [u],
            'change_user': [u],
            'delete_user': [u],
        }

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')
        lookup_field = 'codename'