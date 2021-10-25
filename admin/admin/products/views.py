from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):

    def list_product(self, request): # /api/products - GET
        pass


    def create(self, request): # /api/products - POST
        pass


    def retrieve(self, request, pk=None): # /api/products/<str:id>
        pass


