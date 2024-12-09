from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework import viewsets

from common.models import User
from common.serializers import UserSerializer, GroupSerializer, PermissionSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer