from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Exhibit


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ExhibitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['nfc_id', 'title', 'description', 'image', 'audio']