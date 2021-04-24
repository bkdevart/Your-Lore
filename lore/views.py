from lore.models import Lore
from lore.serializers import LoreSerializer
from rest_framework import generics


class LoreList(generics.ListCreateAPIView):
    queryset = Lore.objects.all()
    serializer_class = LoreSerializer


class LoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lore.objects.all()
    serializer_class = LoreSerializer