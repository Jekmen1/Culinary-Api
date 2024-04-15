from .filters import DishesFilter
from rest_framework import viewsets
from .models import Dishes, Chefs, Rating
from .serializers import DishesSerializer, ChefsSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
class DishesViewSet(viewsets.ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = DishesFilter

class ChefsViewSet(viewsets.ModelViewSet):
    queryset = Chefs.objects.all()
    serializer_class = ChefsSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class Algorithm(viewsets.ModelViewSet):
    pass
