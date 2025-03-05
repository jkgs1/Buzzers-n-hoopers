from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework import viewsets
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