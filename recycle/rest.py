from recycle.models import *
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from django_filters.rest_framework import DjangoFilterBackend


class CatsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','cat_name']

class CatsViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatsSerializer


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_id']

router = DefaultRouter()
router.register('category', CatsViewSet)
router.register('products', ProductViewSet)
