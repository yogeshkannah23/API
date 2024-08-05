from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import *
from django.forms.models import model_to_dict
from api.serializers import ProductSerializers
from rest_framework import generics,mixins,authentication,permissions
from api.permissions import isStaffEditorPermission
# Create your views here.


@api_view(["POST","GET"])
def api_home(request,*args, **kwargs):
    # body = request.body
    # print(request.GET)
    # print(request.POST)
    # print(body)
    # try:
    #     body = json.loads(body)
    #     print(body)
    # except:
    #     pass
    # data={} 
    # data['headers'] = dict(request.headers) 
    # data['content'] = request.content_type
    # print(data)

    # product = Product.objects.all().order_by("?").first()
    
    # product_data = model_to_dict(product)

    # product_data = ProductSerializers(product).data
    product_data = "Not a valid data"
    serializer=ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data,"hi")
    
    return Response(request.data)


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()    
    serializer_class = ProductSerializers


class ProductCreateApiView(generics.CreateAPIView): 
    # queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        print(serializer.validated_data)
        content =  serializer.validated_data.get('content') or None
        if content == "None":
            title = serializer.validated_data.get("title")
            serializer.save(content = title) 
        else:
            serializer.save()

class ProductListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductUpdateView(generics.UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication
                              ]
    permission_classes = [isStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializers

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ProductMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    
    


