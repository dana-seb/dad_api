from rest_framework import serializers

from stats.models import Stat


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ("name", "born", "nationality", "height", "weight")