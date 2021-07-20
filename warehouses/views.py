from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Warehouse
from .permissions import IsOwnerOrReadOnly
from .serializers import WarehouseSerializer


class WarehouseList(ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    template_name = "my_warehouses.html"
    model = Warehouse

