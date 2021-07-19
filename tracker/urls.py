from django.urls import path
from warehouses.views import WarehouseList, WarehouseDetail

urlpatterns = [
  path("", WarehouseList.as_view(), name='warehouse_list'),
  path("<int:pk>/", WarehouseDetail.as_view(), name='warehouse_detail'),
]