from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from warehouses.models import Warehouse
from warehouses.permissions import IsOwnerOrReadOnly
from warehouses.serializers import WarehouseSerializer

class WarehouseListView(ListView):
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = Warehouse.objects.filter(owner=user)
    #     return queryset
    serializer_class = WarehouseSerializer
    template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDetail(DetailView):
    # template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseCreate(CreateView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = WarehouseSerializer
    # template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDelete(DeleteView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = WarehouseSerializer
    # template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseUpdate(UpdateView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = WarehouseSerializer
    # template_name = "my_warehouses.html"
    model = Warehouse
