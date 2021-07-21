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
    fields = ["name","owner","description"]

class WarehouseDelete(DeleteView):
    template_name = "warehouse_delete_view.html"
    model = Warehouse
    success_url = reverse_lazy("my_warehouses")

class WarehouseUpdate(UpdateView):
    template_name = "warehouse_update_view.html"
    model = Warehouse
    fields = ["name","owner","description"]

# @permission_required('admin.can_add_log_entry')
# def inventory_upload(request):
#     template = 'warehouse_detail_view.html'
#     prompt = {'order': 'Order of the CSV should be item, inventory, sales, recieved'}
#     if request == 'GET':
#         return render(request, template, prompt)
#     csv_file = request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'This is not a csv file')
#     data_set = csv_file.read().decode('utf-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=','):
#         _, created = Inventory.objects.update_or_create(
#             item=column[0],
#             inventory=column[1],
#             sales=column[2],
#             recieved=column[3],
#         )
#     context = {}
#     return render(request, template, context)
