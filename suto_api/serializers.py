from rest_framework import serializers
from suto_api.models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('name', 'type', 'photo_main_little', 'price')