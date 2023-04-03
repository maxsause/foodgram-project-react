import django_filters
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db.utils import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend, \
    ModelMultipleChoiceFilter, FilterSet
from rest_framework import mixins, status, viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.permissions import (
    SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAuthenticated)
from rest_framework.response import Response

from django_filters import NumberFilter

from recipe.models import Tag, Recipe, Favorite, ShoppingCart
from .serializers import (TagSerializer, RecipeGetSerializer,
                          RecipePostSerializer, ShoppingCartSerializer,
                          SubscriptionSerializer)
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .filters import RecipeFilter

User = get_user_model()


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeGetSerializer
        return RecipePostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # @action(
    #     detail=True, methods=['POST', 'DELETE'],
    #     permission_classes=(IsAuthenticated,)
    # )
    # def favorite(self, request, pk):
    #     recipe = get_object_or_404(Recipe, pk=pk)
    #     if request.method == 'POST':
    #         favorite, created = Favorite.objects.get_or_create(
    #             user=request.user,
    #             recipe=recipe
    #         )
    #         if created:
    #             serializer = FavoriteSerializer(favorite)
    #             return Response(
    #                 serializer.data,
    #                 status=status.HTTP_201_CREATED
    #             )
    #         else:
    #             return Response(
    #                 {'errors': (
    #                                 f'Рецепт "{recipe}" '
    #                                 'уже добавлен в Избранное'
    #                             )},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )
    #     if request.method == 'DELETE':
    #         try:
    #             Favorite.objects.get(user=request.user, recipe=recipe).delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
    #         except ObjectDoesNotExist:
    #             return Response(
    #                 {'errors': (
    #                                 f'Рецепт "{recipe}" не '
    #                                 'находился в Избранном'
    #                             )},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )
    #         except Exception as other_exception:
    #             return Response(
    #                 {'errors': str(other_exception)},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )


class ShoppingCartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        user = self.request.user
        return user.cart.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriptionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return self.request.user.follower.all()
