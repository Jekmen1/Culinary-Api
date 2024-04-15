from django_filters import rest_framework as filters
from .models import Dishes

class DishesFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    description = filters.CharFilter(lookup_expr="icontains")
    Preparation_methods = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Dishes
        fields = ['title', 'description', 'Preparation_methods']