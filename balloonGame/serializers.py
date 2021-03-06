from rest_framework import serializers
from .models import balloonGameData

class balloonGameDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = balloonGameData
        fields = ('emailId', 'color', 'clicksBursted', 'clicksCollected', 'amountCollected', 'total')