from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from warehouses.models import Warehouse
from django.urls import reverse_lazy

class WarehouseListView(ListView):
    template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDetail(DetailView):
    template_name = "warehouse_detail_view.html"
    model = Warehouse

class WarehouseCreate(CreateView):
    template_name = "warehouse_create_view.html"
    model = Warehouse
    fields = ["name","owner","description","length","width","height","lane_width_size","shelf_length","shelf_depth","shelf_height"]

class WarehouseDelete(DeleteView):
    template_name = "warehouse_delete_view.html"
    model = Warehouse
    success_url = reverse_lazy("my_warehouses")

class WarehouseUpdate(UpdateView):
    template_name = "warehouse_update_view.html"
    model = Warehouse
    fields = ["name","owner","description","length","width","height","lane_width_size","shelf_length","shelf_depth","shelf_height"]

