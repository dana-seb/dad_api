from rest_framework import generics

from stats.models import Stat
from .serializers import StatSerializer


class StatAPIView(generics.ListAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

