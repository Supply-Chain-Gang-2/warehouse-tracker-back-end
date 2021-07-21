from django.urls import path
from .views import WarehouseCreate, WarehouseDelete, WarehouseListView, WarehouseUpdate, WarehouseDetail

urlpatterns = [
    path("", WarehouseListView.as_view(), name='my_warehouses'),
    path("<int:pk>/", WarehouseDetail.as_view(), name='warehouse_detail_view'),
    path("create/", WarehouseCreate.as_view(), name='create'),
    path("update/<int:pk>/", WarehouseUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", WarehouseDelete.as_view(), name='delete'),
]
