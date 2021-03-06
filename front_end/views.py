import csv, io
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from warehouses.models import Warehouse, Item
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from accounts.forms import CustomUserCreationForm

class WarehouseListView(ListView):
    template_name = "my_warehouses.html"
    model = Warehouse

class WarehouseDetail(DetailView):
    template_name = "warehouse_detail_view.html"
    model = Warehouse
    def get_context_data(self, **kwargs):
        context = super(WarehouseDetail, self).get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

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

# @permission_required('admin.can_add_log_entry')
def inventory_upload(request, **kwargs):
    csv_file = request.FILES['file']
    warehouse_id = request.POST.get('warehouse_id')
    warehouse_name = request.POST.get('warehouse_name')
    my_var = Warehouse.objects.get(name=warehouse_name)
    print(my_var, '--------------HELLO-------------------')
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Item.objects.update_or_create(
            warehouse=my_var,
            item_name=column[0],
            units_in_inventory=column[1],
            units_sold=column[2],
            units_recieved=column[3],
        )
    context = {}
    return redirect('warehouse_detail_view', pk=warehouse_id)

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('my_warehouses')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register.html', {'form': f})

