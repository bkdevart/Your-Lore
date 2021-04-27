from rest_framework import serializers
from lore.models import Lore
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    lore = serializers.PrimaryKeyRelatedField(many=True, queryset=Lore.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'lore']

class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'title', 'story', 'owner']