from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, RecipeViewSet, ShoppingCartViewSet, \
    SubscriptionsViewSet

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register(r'recipes/(?P<id>[1-9]\d*)/shopping_cart', ShoppingCartViewSet, basename='shopping_cart')
# router.register(r'')
router.register(r'users/(?P<id>[1-9]\d*)/subscribe', SubscriptionsViewSet, basename='subscribe')
#router.register(r'')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
