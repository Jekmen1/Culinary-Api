from rest_framework import serializers
from .models import Dishes, Chefs, Rating

class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'


class ChefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chefs
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'