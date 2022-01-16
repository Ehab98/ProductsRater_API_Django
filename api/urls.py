

from django.urls import path ,include
from .import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('product',views.ProductViewset)
router.register('rating',views.RatingViewset)


urlpatterns = [
    path('',include(router.urls) ),
    
]
