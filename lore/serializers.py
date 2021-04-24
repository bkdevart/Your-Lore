from rest_framework import serializers
from lore.models import Lore


class LoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lore
        fields = ['id', 'title', 'story']