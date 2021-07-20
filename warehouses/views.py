from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Warehouse
from .permissions import IsOwnerOrReadOnly
from .serializers import WarehouseSerializer

class WarehouseList(ListCreateAPIView):
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Warehouse.objects.filter(owner=user)
    #     return queryset
    serializer_class = WarehouseSerializer
    template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    def get_queryset(self):
        user = self.request.user
        queryset = Warehouse.objects.filter(owner=user)
        return queryset
    serializer_class = WarehouseSerializer
    template_name = "my_warehouses.html"
    model = Warehouse
