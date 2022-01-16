from django.shortcuts import render
from rest_framework import viewsets
from .models import Product , Rating
from .serializers import ProductSerializer , RatingSerializer

# Create your views here.

#API With View sets -->> iy`s allowed me to make crud operation 
class ProductViewset (viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RatingViewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class = RatingSerializer
