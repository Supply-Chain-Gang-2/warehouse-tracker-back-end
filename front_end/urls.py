from django.urls import path
from .views import WarehouseCreate, WarehouseDelete, WarehouseListView, WarehouseUpdate, WarehouseDetail, inventory_upload, register

urlpatterns = [
    path("", WarehouseListView.as_view(), name='my_warehouses'),
    path("<int:pk>/", WarehouseDetail.as_view(), name='warehouse_detail_view'),
    path("create/", WarehouseCreate.as_view(), name='warehouse_create_view'),
    path("<int:pk>/update/", WarehouseUpdate.as_view(), name='warehouse_update_view'),
    path("<int:pk>/delete/", WarehouseDelete.as_view(), name='warehouse_delete_view'),
    path("<int:pk>/upload/", inventory_upload, name='my_warehouses'),
    path("register/", register, name='register')
]
