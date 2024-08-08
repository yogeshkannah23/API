from rest_framework import serializers,reverse
from api.models import Product



class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url_edit = serializers.HyperlinkedIdentityField(
        view_name= 'product-edit',
        lookup_field = 'pk',
    )
    class Meta:
        model = Product
        fields=[
            'id',
            'url',
            'url_edit',
            'title',
            'content',
            'sale_price',
            'my_discount'
        ]

    def validate_title(self,value):
        qs = Product.objects.filter(title__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already present in database")
        return value
    
    def get_my_discount(self,obj):
        try:
            if obj.id == 1:
                return "There is no discount for this product"
            return obj.discount()
        except:
            return None

    def get_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail',kwargs={'pk':obj.id},request=request)