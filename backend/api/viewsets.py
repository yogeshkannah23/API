from api.models import Product
from rest_framework import viewsets

from api.serializers import ProductSerializers


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    