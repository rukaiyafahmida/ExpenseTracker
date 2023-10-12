from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from core.models import Currency, Category
from core.serializers import CurrencySerializer, CategorySerializer

class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer