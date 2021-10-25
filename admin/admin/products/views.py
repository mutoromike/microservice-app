from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):

    def list_products(self, request): # /api/products - GET
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # /api/products - POST
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def update(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)

        pass


