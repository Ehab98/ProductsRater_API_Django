from pyexpat import model
from rest_framework import serializers
from .models import Product , Rating


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ('id', 'name','description')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','product','user','stars')
