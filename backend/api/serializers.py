from rest_framework import serializers
from api.models import Product



class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields=[
            'id',
            'title',
            'content',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self,obj):
        try:
            if obj.id == 1:
                return "There is no discount for this product"
            return obj.discount()
        except:
            return None