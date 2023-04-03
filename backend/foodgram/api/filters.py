from django_filters import ModelMultipleChoiceFilter, NumberFilter
from django_filters.rest_framework import FilterSet

from recipe.models import Tag, Recipe


class RecipeFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )
    is_favorited = NumberFilter()
    is_in_shopping_cart = NumberFilter()

    class Meta:
        model = Recipe
        fields = ('tags',)
