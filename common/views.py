from django.contrib.auth.models import Group, Permission, AnonymousUser
from guardian.utils import get_anonymous_user
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_guardian import filters

from common.models import User
from common.permissions import ObjectPermissions
from common.serializers import UserSerializer, GroupSerializer, PermissionSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [ObjectPermissions]
    filter_backends = [filters.ObjectPermissionsFilter]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = [ObjectPermissions]
    filter_backends = [filters.ObjectPermissionsFilter]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    permission_classes = [ObjectPermissions]
    filter_backends = [filters.ObjectPermissionsFilter]


class ObtainAuthOrAnonToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # If empty post sent, return an anonymous user token
        if not request.data:
            token, created = Token.objects.get_or_create(user=get_anonymous_user())
            return Response({'token': token.key})
        else:
            return super().post(request, *args, **kwargs)
